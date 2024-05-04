import pyautogui
from pyKey import pressKey, releaseKey, press, sendSequence, showKeys

NOTEPAD = pyautogui.getWindowsWithTitle("Rocket League")[0]
NOTEPAD.activate()

press(key='W', sec=2)
press(key='BSLASH')