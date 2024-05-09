# Project: AI Gamer
# Author: Marcel Pratikto
# Date created: May 4, 2024
# Description: This program uses AI to play the game Rocket League
 
import cv2 as cv # OpenCV computer vision library
import numpy as np # Scientific computing library
import pyautogui
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys
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
cam = cv.VideoCapture(1, cv.CAP_DSHOW)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 1024)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 768)
 
pb  = 'Code/frozen_inference_graph.pb'
pbt = 'Code/ssd_inception_v2_coco_2017_11_17.pbtxt'
 
# Read the neural network
cvNet = cv.dnn.readNetFromTensorflow(pb,pbt)   

# Make sure that Rocket League is running
# then switch focus to it
RL = pyautogui.getWindowsWithTitle("Rocket League")[0]
RL.activate()

# TODO keys
FORWARD = 'W'
BACKWARD = 'S'
LEFT = 'A'
RIGHT = 'D'
JUMP = 'SPACEBAR'

# TODO Last known position of ball
# TODO use size as an indicator if ball is coming towards the player or moving away
ball_x = 0
ball_y = 0
ball_width = 0

# TODO random ???
#random.seed()

while True:

  # TODO start with ball not detected
  ball_detected = False

  # Read in the frame
  ret_val, img = cam.read()
  rows = img.shape[0]
  cols = img.shape[1]
  cvNet.setInput(cv.dnn.blobFromImage(img, size=(1024, 768), swapRB=True, crop=False)) # default size=(300,300)
 
  # Run object detection
  cvOut = cvNet.forward()
 
  # Go through each object detected and label it
  for detection in cvOut[0,0,:,:]:
    score = float(detection[2])
    if score > 0.3:
 
      idx = int(detection[1])   # prediction class index. 
 
      # If a ball is found
      if classes[idx] == 'sports ball': # or classes[idx] == 'car':      
        left = detection[3] * cols
        top = detection[4] * rows
        right = detection[5] * cols
        bottom = detection[6] * rows
        cv.rectangle(img, (int(left), int(top)), (int(right), int(bottom)), (23, 230, 210), thickness=2)
            
        # draw the prediction on the frame        
        # label = "{}: {:.2f}%".format(classes[idx],score * 100)
        x = left
        y = bottom
        width = right - left

        label = "x:{:.2f}, y:{:.2f}, width:{:.2f}".format(x, y, width)
        y = top - 15 if top - 15 > 15 else top + 15
        cv.putText(img, label, (int(left), int(y)),cv.FONT_HERSHEY_SIMPLEX, 0.5, colors[idx], 2)
        
        # TODO tell the program if we detected a ball
        ball_detected = True
 
  # Display the frame
  cv.imshow('my webcam', img)

  # Press ESC to quit
  if cv.waitKey(1) == 27: 
    break

  if ball_detected:
  # TODO Do actions if ball was detected
    press(key=JUMP)
  else:
  # TODO if ball was not detected
    r = random.randint(1,4)
    print(r)
    if r == 1:
      press(key=FORWARD)
    elif r == 2:
      press(key=BACKWARD)
    elif r == 3:
      press(key=LEFT)
    else:
      press(key=RIGHT)
 
# Stop filming
cam.release()
 
# Close down OpenCV
cv.destroyAllWindows()