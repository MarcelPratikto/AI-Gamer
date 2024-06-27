"""
Project: AI Gamer
Author: Marcel Pratikto
Date created: May 4, 2024
Description: This program uses AI to play the game Rocket League
"""

#-------------------------------------------------------------------------------------------------------
# IMPORTS
#-------------------------------------------------------------------------------------------------------
import cv2 as cv    # OpenCV computer vision library
import numpy as np  # Scientific computing library
import time         # 
import pyautogui    # switch focus between programs
import csv
import os.path
# gamepad related stuff
from inputs import get_gamepad
import math
import threading

#-------------------------------------------------------------------------------------------------------
# XBOX Controller Class
#-------------------------------------------------------------------------------------------------------
class XboxController(object):
  MAX_TRIG_VAL = math.pow(2, 8)
  MAX_JOY_VAL = math.pow(2, 15)

  def __init__(self):
    self.LeftJoystickY = 0
    self.LeftJoystickX = 0
    self.RightJoystickY = 0
    self.RightJoystickX = 0
    self.LeftTrigger = 0
    self.RightTrigger = 0
    self.LeftBumper = 0
    self.RightBumper = 0
    self.A = 0
    self.X = 0
    self.Y = 0
    self.B = 0
    self.LeftThumb = 0
    self.RightThumb = 0
    self.Back = 0
    self.Start = 0
    self.LeftDPad = 0
    self.RightDPad = 0
    self.UpDPad = 0
    self.DownDPad = 0

    self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
    self._monitor_thread.daemon = True
    self._monitor_thread.start()

  def read(self): # return the buttons/triggers that you care about in this method
    x = self.LeftJoystickX
    y = self.LeftJoystickY
    rt = self.RightTrigger
    lt = self.LeftTrigger
    X = self.X # b=1, x=2
    A = self.A
    B = self.B
    rightDPad = self.RightDPad
    end_button = self.RightBumper
    reset_button = self.LeftBumper
    return [x, y, rt, lt, X, A, B, rightDPad, end_button, reset_button] # make sure that the last two items are end_button and reset_button

  def _monitor_controller(self):
    while True:
      events = get_gamepad()
      for event in events:
        if event.code == 'ABS_Y':
          self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        elif event.code == 'ABS_X':
          self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        elif event.code == 'ABS_RY':
          self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        elif event.code == 'ABS_RX':
          self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
        elif event.code == 'ABS_Z':
          self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
        elif event.code == 'ABS_RZ':
          self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
        elif event.code == 'BTN_TL':
          self.LeftBumper = event.state
        elif event.code == 'BTN_TR':
          self.RightBumper = event.state
        elif event.code == 'BTN_SOUTH':
          self.A = event.state
        elif event.code == 'BTN_NORTH':
          self.Y = event.state #previously switched with X
        elif event.code == 'BTN_WEST':
          self.X = event.state #previously switched with Y
        elif event.code == 'BTN_EAST':
          self.B = event.state
        elif event.code == 'BTN_THUMBL':
          self.LeftThumb = event.state
        elif event.code == 'BTN_THUMBR':
          self.RightThumb = event.state
        elif event.code == 'BTN_SELECT':
          self.Back = event.state
        elif event.code == 'BTN_START':
          self.Start = event.state
        elif event.code == 'BTN_TRIGGER_HAPPY1':
          self.LeftDPad = event.state
        elif event.code == 'BTN_TRIGGER_HAPPY2':
          self.RightDPad = event.state
        elif event.code == 'BTN_TRIGGER_HAPPY3':
          self.UpDPad = event.state
        elif event.code == 'BTN_TRIGGER_HAPPY4':
          self.DownDPad = event.state

#-------------------------------------------------------------------------------------------------------
# OPENCV
#-------------------------------------------------------------------------------------------------------
# Just use a subset of the classes
classes = ["background", "person", "bicycle", "car", "motorcycle",
  "airplane", "bus", "train", "truck", "boat", "traffic light", "fire hydrant",
  "unknown", "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse",
  "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "unknown", "backpack",
  "umbrella", "unknown", "unknown", "handbag", "tie", "suitcase", "frisbee", "skis",
  "snowboard", "sports ball", "kite", "baseball bat", "baseball glove", "skateboard",
  "surfboard", "tennis racket", "bottle", "unknown", "wine glass", "cup", "fork", "knife",
  "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli", "carrot", "hot dog",
  "pizza", "donut", "cake", "chair", "couch", "potted plant", "bed", "unknown", "dining table",
  "unknown", "unknown", "toilet", "unknown", "tv", "laptop", "mouse", "remote", "keyboard",
  "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "unknown",
  "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

# Colors we will use for the object labels
colors = np.random.uniform(0, 255, size=(len(classes), 3))
 
# Open the webcam
# switch between 0 or 1 if the correct webcam isn't showing
cam = cv.VideoCapture(0, cv.CAP_DSHOW)
WIDTH = 1024
HEIGHT = 768
cam.set(cv.CAP_PROP_FRAME_WIDTH, WIDTH)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, HEIGHT)
 
pb  = 'Code/frozen_inference_graph.pb'
pbt = 'Code/ssd_inception_v2_coco_2017_11_17.pbtxt'

# Read the neural network
cvNet = cv.dnn.readNetFromTensorflow(pb,pbt)   

#-------------------------------------------------------------------------------------------------------
# GAMEPAD, CSV
#-------------------------------------------------------------------------------------------------------
# Save gamepad controls to csv file to train AI model
csv_file_path = "Code/sample.csv"
is_file_new = True
if os.path.isfile(csv_file_path): # if file already exist, it is not new and we don't need to csv_writer.writeheader()
  is_file_new = False
csv_file = open(csv_file_path, "a", newline="")
field_names = [
  "time_elapsed",
  "ball_detected",
  "ball_x",
  "ball_y",
  "ball_width",
  "joystick_x",
  "joystick_y",
  "RT_intensity",
  "LT_intensity",
  "btn_X",
  "btn_A",
  "btn_B",
  "reset",
  "end"
]
csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
# only writeheader when starting a new csv file to store data in
if is_file_new:
  csv_writer.writeheader()

# xbox controller for monitoring inputs
# Only activate when storing gamepad inputs to csv file
xbc = XboxController()

#-------------------------------------------------------------------------------------------------------
# BALL
#-------------------------------------------------------------------------------------------------------
# Last known position of ball on the screen
ball_x = -1
ball_y = -1
# How close the ball is to the screen
ball_width = -1

# start with ball not detected
ball_detected = False

#-------------------------------------------------------------------------------------------------------
# MAIN LOOP
#-------------------------------------------------------------------------------------------------------
# Make sure that Rocket League is running then switch focus to it
RL = pyautogui.getWindowsWithTitle("Rocket League")[0]
RL.activate()

# sytem time of when the program starts
start_time = time.time()

while True:
  # start with ball not detected
  # ball_x = -1
  # ball_y = -1
  # ball_width = -1
  # ball_detected = False

  # Read in the frame
  ret_val, img = cam.read()
  rows = img.shape[0]
  cols = img.shape[1]
  w = 900
  h = 900
  cvNet.setInput(cv.dnn.blobFromImage(img, size=(w, h), swapRB=True, crop=False)) # default size=(300,300)
 
  # Run object detection
  cvOut = cvNet.forward()

  # time elapsed since starting this program
  current_time = time.time()
  time_elapsed = current_time - start_time

  # Go through each object detected and label it
  for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.2:
 
      idx = int(detection[1])   # prediction class index. 
 
      # If a ball is found
      if classes[idx] == 'sports ball': # or classes[idx] == 'car':      
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)

        # store the ball position
        ball_x = left
        ball_y = bottom
        ball_width = right - left
        # tell the program we detected a ball
        ball_detected = True

        # draw the prediction on the frame        
        # label = "{}: {:.2f}%".format(classes[idx],score * 100)
        label = "x:{:.2f}, y:{:.2f}, width:{:.2f}".format(ball_x, ball_y, ball_width)
        y = top - 15 if top - 15 > 15 else top + 15
        # cv.putText(img, label, (int(left), int(y)),cv.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)
        # (image, text, point, font face, font scale, color, thickness)
        cv.putText(img, label, (int(left), int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)

  # reads the gamepad buttons
  buttons = xbc.read()

  csv_writer.writerow({       # If you add anything else, UPDATE field_names and xbc.read()
    field_names[0]:   time_elapsed,
    field_names[1]:   ball_detected,
    field_names[2]:   ball_x,
    field_names[3]:   ball_y,
    field_names[4]:   ball_width,
    field_names[5]:   buttons[0], # Left joystick x
    field_names[6]:   buttons[1], # Left joystick y
    field_names[7]:   buttons[2], # RT intensity
    field_names[8]:   buttons[3], # LT intensity
    field_names[9]:   buttons[4], # X
    field_names[10]:  buttons[5], # B
    field_names[11]:  buttons[6], # A
    field_names[13]:  buttons[-1],# reset_button
    field_names[14]:  buttons[-2] # end_button
  })

  if buttons[-1] == 1:      # Make sure that the last item in buttons[] is the reset_button
  #   # if the reset_button is pressed,
  #   # it will reset start_time, ball_detected, and the ball position and width
    # start_time = time.time()
    ball_detected = False
    ball_x = -1
    ball_y = -1
    ball_width = -1

  if buttons[-2] == 1:      # Make sure that the second to last item in buttons[] is the end_button
    # if the end_button is pressed,
    # end the AI-Gamer program by exiting out of the main while loop
    break

  # Display the frame
  cv.imshow('AI-Gamer', img)

  # Press ESC to quit
  if cv.waitKey(1) == 27:
    break

#-------------------------------------------------------------------------------------------------------
# EXIT FROM MAIN LOOP
#-------------------------------------------------------------------------------------------------------
# Stop filming
cam.release()

# Close down OpenCV
cv.destroyAllWindows()

# Close file
csv_file.close()