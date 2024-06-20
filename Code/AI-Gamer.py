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
import pickle       # load ML model
import vgamepad as vg   # gamepad related stuff

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
# ML model
#-------------------------------------------------------------------------------------------------------
model = pickle.load(open("Code/model.pkl", "rb"))

#-------------------------------------------------------------------------------------------------------
# GAMEPAD
#-------------------------------------------------------------------------------------------------------
# TODO activate gamepad
# Only activate when NOT storing gamepad inputs to csv file
gamepad = vg.VX360Gamepad()

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

  # use the ml model to make predictions on what buttons on the gamepad are pressed & how intensely if possible
  buttons = model.predict([[
        time_elapsed,
        ball_detected,
        ball_x,
        ball_y,
        ball_width
    ]])
  
  joystick_x = buttons[0][0]
  joystick_y = buttons[0][1]
  RT_intensity = buttons[0][2]
  LT_intensity = buttons[0][3]
  btn_X = buttons[0][4]
  btn_A = buttons[0][5]
  btn_B = buttons[0][6]
  reset = buttons[0][7]

  gamepad.left_joystick_float(x_value_float=joystick_x, y_value_float=joystick_y)
  gamepad.right_trigger_float(RT_intensity)
  gamepad.left_trigger_float(LT_intensity)
  if btn_X:
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
  if btn_A:
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
  if btn_B:
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
  gamepad.update()

  if reset == 1:      # Make sure that the last item in buttons[] is the reset_button
  #   # if the reset_button is pressed,
  #   # it will reset start_time, ball_detected, and the ball position and width
    # start_time = time.time()
    ball_detected = False
    ball_x = -1
    ball_y = -1
    ball_width = -1

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