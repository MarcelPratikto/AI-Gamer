# AI Gamer

This program will use AI to play the game Rocket League

### Sources

Gamepad
* https://pypi.org/project/vgamepad/

Keyboard
* https://github.com/gauthsvenkat/pyKey 

Screen / switching between programs:
* https://www.reddit.com/r/learnpython/comments/xb10do/how_do_i_switch_between_open_programs_with_python/ 
* https://pyautogui.readthedocs.io/en/latest/

TensorFlow Object Detection:
* https://automaticaddison.com/how-to-load-a-tensorflow-model-using-opencv/
* https://github.com/opencv/opencv/wiki/TensorFlow-Object-Detection-API

TODO: Train AI Neural Network using my gameplay style
* Figure out how to write to a csv file
    * https://www.geeksforgeeks.org/how-to-open-and-close-a-file-in-python/
    * https://docs.python.org/3/library/csv.html
* Read and store gamepad inputs to a csv file
    * https://stackoverflow.com/questions/46506850/how-can-i-get-input-from-an-xbox-one-controller-in-python
    * https://pypi.org/project/inputs/
* Save and load model
    * https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/keras/save_and_load.ipynb
    * https://www.geeksforgeeks.org/saving-a-machine-learning-model/
    * https://colab.research.google.com/gist/MarcelPratikto/d62275bac7d93282a885eb4e5c98717b/simple_nn_example.ipynb#scrollTo=w1jKaZouuVta

Multi Output Regressor:
* https://gist.github.com/MarcelPratikto/d62275bac7d93282a885eb4e5c98717b
* https://medium.com/@tubelwj/developing-multi-class-regression-models-with-python-c8beca5dd482
* https://scikit-learn.org/stable/modules/generated/sklearn.multioutput.MultiOutputRegressor.html
* https://stackoverflow.com/questions/57704609/multi-target-regression-using-scikit-learn
* https://machinelearningmastery.com/multi-output-regression-models-with-python/

My ML model:
* https://colab.research.google.com/drive/1p0dx8kcFgv25ZtLTsFrDm-mUqmSyD1tg#scrollTo=vEjxMsHGNuHP

Categories:
* Input
    * Time elapsed in-game
    * Ball detected
    * Ball x
    * Ball y
    * Ball width
* Output
    * Left joystick x
    * Left joystick y
    * RT intensity
    * LT intensity
    * X button pressed
    * A button pressed
    * B button pressed
    * reset_button pressed
    * end_button pressed