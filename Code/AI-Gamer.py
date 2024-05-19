# Project: AI Gamer
# Author: Marcel Pratikto
# Date created: May 4, 2024
# Description: This program uses AI to play the game Rocket League
 
import cv2 as cv # OpenCV computer vision library
import numpy as np # Scientific computing library
import pyautogui
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
import time
import random
 
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
  "book", "clock", "vase", "scissors", "teddy bear", "hair drier", "toothbrush" ]
 
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

# Make sure that Rocket League is running then switch focus to it
RL = pyautogui.getWindowsWithTitle("Rocket League")[0]
RL.activate()

# TODO keys
# MAKE SURE LETTERS ARE IN LOWERCASE OR pyKey WILL HOLD SHIFT!!!
#seq_keys = []
FORWARD = 'w'
BACKWARD = 's'
LEFT = 'a'
RIGHT = 'd'
JUMP = 'SPACEBAR'

# TODO Last known position of ball
# TODO use size as an indicator if ball is coming towards the player or moving away
ball_x = 0
ball_y = 0
ball_width = 0

# TODO start with ball not detected
ball_detected = False
initial_move = 0.0

# TODO zig-zag until ball is detected
zig = 0.0
zag = False

while True:
  # Read in the frame
  ret_val, img = cam.read()
  rows = img.shape[0]
  cols = img.shape[1]
  cvNet.setInput(cv.dnn.blobFromImage(img, size=(WIDTH, HEIGHT), swapRB=True, crop=False)) # default size=(300,300), alternates: (1024,768), (800,600)
 
  # Run object detection
  cvOut = cvNet.forward()
 
  # Go through each object detected and label it
  for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.7:
 
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
        # if ball_width > 50.0:
        #   ball_detected = True
        #   #print(f"Ball x:{ball_x}, y:{ball_y}, width:{ball_width}")
        ball_detected = True

        # draw the prediction on the frame        
        # label = "{}: {:.2f}%".format(classes[idx],score * 100)
        label = "x:{:.2f}, y:{:.2f}, width:{:.2f}".format(ball_x, ball_y, ball_width)
        y = top - 15 if top - 15 > 15 else top + 15
        # cv.putText(img, label, (int(left), int(y)),cv.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)
        # (image, text, point, font face, font scale, color, thickness)
        cv.putText(img, label, (int(left), int(y)), cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 2)
 
  # Display the frame
  cv.imshow('my webcam', img)

  # Press ESC to quit
  if cv.waitKey(1) == 27: 
    break

  if ball_detected:
  # TODO Do actions if ball was detected
    # press(key=JUMP, sec=1)
    r = random.randint(1,3)
  else:
  # TODO if ball was not detected
    if initial_move == 0.0:
      press(key=FORWARD, sec=2)
      initial_move = time.time()
    current_time = time.time()
    if current_time - initial_move > 3.0:
      if zig == 0.0:
        pressKey(key=FORWARD)
        press(key=LEFT, sec=1)
        releaseKey(key=FORWARD)
        zig = time.time()
      else:
        current_time = time.time()
        time_elapsed = current_time - zig
        if not zag and (time_elapsed > 3.0):
          pressKey(key=FORWARD)
          press(key=RIGHT, sec=1)
          releaseKey(key=FORWARD)
          zag = True
        else:
          if time_elapsed > 6.0:
            zig = 0.0
            zag = False
 
# Stop filming
cam.release()
 
# Close down OpenCV
cv.destroyAllWindows()