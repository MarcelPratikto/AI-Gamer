**Name:** Marcel Pratikto

**Project Title:** AI Gamer

**Team Members:**
1. Marcel Pratikto

**Overall Status:**
![50%](https://progress-bar.dev/50?title=Progress)

**Number of hours worked since last update:** 9

**Number of hours worked on the project thus far:** 81

**Total number of hours anticipated for completion:** 130

**Accomplishments:**

I was able to do some data analysis of my dataset.

This chart shows the relationships between all the different featured variables. The main thing to get from this correlation matrix is that ball_detected is the best indicator of a ball's x and y positions (ball_x, ball_y) and that time_elapsed is the best overall indicator of the different variables.

![Screenshot1](C:/GitHub/AI-Gamer/Screenshots/2024-06-15-Correlation-Matrix.png)

This charts shows the distribution of the target variables that aren't binary. This will be important to figure out the probability of the ML model outputting those values to the virtual gamepad.

![Screenshot2](C:/GitHub/AI-Gamer/Screenshots/2024-06-15-Distribution.png)

This one is perhaps the most important obeservation: which type of machine learning model to use. The lower the Mean Square Error (MSE) and Mean Absolute Error (MAE), the lower the chances of an error and the better the performance.

![Screenshot2](C:/GitHub/AI-Gamer/Screenshots/2024-06-15-ML-Scores.png)

I will be using the random forest model.

**Challenges:**

* Training the dataset is taking a long time, there is no shortcut to train the data to emulate my playstyle in Rocket League. I will need to keep training the dataset to have a more accurate gamepad output.

**Plans / Goals for next week:**

1. Figure out how to save and export the ML model from Google Colab so that it can be used with the program in my computer.
2. More dataset training.

**Accountability plan: (What is your plan to keep yourself honest and follow through with the goals that you have outlined?)**

I will have my roommate make sure that I work on this at least 2 hours per day when I am not busy working on my other classes

**Other comments:**

N/A