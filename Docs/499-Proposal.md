# CSE499 - Project Proposal
## Marcel Pratikto

#### 1. Project Name
AI Gamer

#### 2. Group Size / Contact Information
1. Marcel Pratikto / pra14016@byui.edu / 267-356-7568

#### 3. Abstract / Purpose
The **purpose** of this project is to learn how to create, train, and apply an AI to a real-world activity. In this case, the real-world activity is to play video games.
The **objective** of this project is to get an AI to aim and hit the ball in the video game Rocket League.

#### 4. Background / Prior Knowledge
On the subject of AI, I would consider myself a beginner.
I major in CS with an emphasis in Machine Learning, so I have a bit of experience through classes such as:
* CSE 450     Machine Learning        <-- The class that got me interested in this subject
* DS 460      Big Data Programming

This project will build on work that has been done by others, including but not limited to:
* Image recognition software
* Machine learning models
* Python libraries such as numpy, tensorflow

Available resources (initial research):
* [Real Time Object Recognition Using Webcam, Deep Learning](https://automaticaddison.com/real-time-object-recognition-using-a-webcam-and-deep-learning/)
* [TensorFlow Object detection API Tutorial](https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/auto_examples/object_detection_camera.html)

Mind map:
* Image recognition
* ML model trained on playing a game
* Keyboard & mouse scripts
* Shell commands

#### 5. Description

##### Why?

Back in the day, there used to be profit in video game farming. This consists of doing repetitive tasks for a long period of time to gain legendary items, attain a certain rank, or reach a specified level. The virtual item or account would then be sold for real money. This is different from hacking, which would use software to exploit vulnerabilities in the game, which is illegal. Video game farming, on the other hand, is technically legal since it is actual people playing the game for hours on end. Imagine if that work was offloaded to an AI. You can gain experience and items by letting your computer run when you're at work. There is no need to deal with sketchy video game farmers.

Another reason to create an AI gamer is for competition. In the days of old, the AIs of the time were created to try to challenge chess grandmasters. It wasn't until 1997 that IBM's Deep Blue AI succeeded in beating the world's grandmaster. If it's possible in chess, that it surely must be possible for an AI to compete in other games as well.

##### What?

This project will create an AI that can play the video game "Rocket League". Rocket League is an online game, similar to the sport soccer, where the objective is to score more goals than the enemy team. The difference is that the players are RC cars that can double jump and fly using rocket boost and there are no rules against playing rough. The AI created will be able to play this game using a webcam as its eye and a keyboard & mouse script as its hands and feet.

##### Who?

The target audience for this project are people that are interested in both video games and AI.

##### Where?

This AI Gamer will be developed and run on the PC.

##### How?

Gamers will use this AI by running my program that will use a webcam for computer vision, feed that info to the AI, then feed the output from the AI to a script that will activate the keyboard & mouse.

##### When?

The project is good enough when the AI can move and hit the ball. Anything past that, such as aiming the ball towards the enemy goal will be added if there is more time available.

#### 6. Significance

My project will be significant because there isn't a lot of AIs being created to play video games. One that I can think of is Google's SIMA. Note that this differs from the Non-Playable Characters (NPCs) programmed within the games themselves, who are also referred to as AI even though they are not. My AI will be playing externally, much like a person playing video games.

#### 7. New Computer Science Concepts

Here are new concepts/skills that I will need to learn for this project:
* Computer Vision
* Keyboard, mouse scripting
* Creating custom data for AI training

#### 8. Interestingness

This project is interesting to me because it combines one of my hobbies, video games, with my profession. It helps that Rocket League is one of my favorite games to play with my buddies. It is one of those games that doesn't require constant maintenance, we just pick up and play whenever we have free time. It is simple enough that we can catch up while playing, but challenging enough to still keep us engaged in the game. It's basically like playing soccer with the boys, but virtually and with rocket boosts.

#### 9. Tasks and Schedule

| Week(s) | Tasks | Goal |
| -- | -- | -- |
| 1 | Brainstorm ideas for project, inital research | Know what to do for senior project |
| 2 | Develop keyboard and mouse scripts | Allow an external program to use controls in Rocket League
| 3 | Research computer vision | Be able to implement this in my program |
| 4 - 5 | Implement computer vision | Program should be able to differentiate between the ball and the players on my screen |
| 6 - 9 | Gather data for ML training | Have a large enough data set for ML |
| 10 - 11 | Train AI | AI should be able to predict where the ball will be, and what actions it will need to take with at least 80% accuracy |
| 12 | SPED Talk & combine computer vision, AI, controls | Finish SPED Talk assignment, AI should be able to hit the ball in Rocket League |
| 13 | Finishing touches | Try to improve AI's reaction time and/or performance |

#### 10. Resources

Hardware
* External webcam

Platform
* Windows

Languages
* Python

Libraries
* Numpy
* Pandas
* Polars
* TensorFlow

IDE
* Visual Studio Code