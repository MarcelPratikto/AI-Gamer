**Name:** Marcel Pratikto

**Project Title:** AI Gamer

**Team Members:**
1. Marcel Pratikto

**Overall Status:**
![40%](https://progress-bar.dev/40?title=Progress)

**Number of hours worked since last update:** 9

**Number of hours worked on the project thus far:** 63

**Total number of hours anticipated for completion:** 130

**Accomplishments:**

![Screenshot](C:/GitHub/AI-Gamer/Screenshots/2024-06-01.png)

* I was able to implement a way to record my movements when I play Rocket League. This consisted of figuring out how to read an xbox controller input, then writing it into a csv file whilst running my program, and the game Rocket League.

**Challenges:**

* I still need to figure out if I can add other input data to the ML. So far, I'm only using:
    1. time_elapsed: How many seconds have passed in the game
    2. ball_detected: If a ball is detected or not
    3. ball_x: x position of the ball on the screen (if it's detected)
    4. ball_y: y position of the ball on the screen (if it's detected)
    5. ball_widt: width of the ball on the screen (if it's detected)
* The issue with the point above is that only time_elapsed in consistent. Everything else there is dependent on if my program can detect a ball, which it doesn't most of the time.
* I have to stop the program and re-record after every goal made in order to have more consistent time_elapsed data.

**Plans / Goals for next week:**

1. Continue recording my gameplays into the csv file.
2. Start figuring out how to create and train a Multi-Output Regressor Machine Learning model.

**Accountability plan: (What is your plan to keep yourself honest and follow through with the goals that you have outlined?)**

I will have my roommate make sure that I work on this at least 2 hours per day when I am not busy working on my other classes

**Other comments:**

N/A