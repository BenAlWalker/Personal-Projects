# Personal-Projects

This repository is an example of Personal Projects that I have completed.

------------------------------------------------------------------------------------------------------

heads_flips.py program that will prompt the user for two inputs, how many heads in a row for a successful trial and how many trials they want to run. 

One trial will run until that many heads in a row is recorded. The Total Flips per trial is uploaded into a dataframe and the df keeps track of the moving average. When the program finishes running it will present the user with a graph showing 3 different things:
1. Scatterplot of total flips per trial
2. Moving average of the amount of flips per trial
3. Expected value of total flips until X heads in a row are seen (2^(X+1) - 2 flips)

This program verifies the Law of Large numbers, as the amount of trials is increased, the closer the moving average becomes to the expected value of flips required.

I also included a plotly graph since I wanted to gain some basic experience with using Plotly.

----------------

Regression.py is a linear regression graphing the Max HR of patients based on age. 

------------
randomwalk.py is a simple random walk over the integers, runs for a specified amount of time.
