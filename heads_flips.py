from random import random
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(columns=["Total Flips", "Total Trials", "Average Flips"])

h_in_row = int(input("How many heads in a row to test for? "))
tests = int(input("How many tests? "))
expected = 2 ** (h_in_row + 1) - 2

total_count = 0


def trial(h_in_row):
    counter = 0
    heads = 0
    trial.total_flips = 0
    trial.positions = []
    while counter < int(h_in_row):
        prob = random()
        if 0 < prob <= .5:  # flipped a heads
            counter += 1  # increase total heads by 1
            heads += 1  # head increase by 1
            trial.total_flips += 1
        else:  # flipped a tails
            counter = 0  # reset counter for new iter
            trial.total_flips += 1
            trial.positions.append(heads)
            heads = 0
        if counter == int(h_in_row):
            trial.positions.append(counter)
            df.loc[len(df.index)] = [trial.total_flips, len(trial.positions), df["Total Flips"].mean()]


for i in range(0, tests):
    trial(h_in_row)

print(df)

plt.axhline(y=expected, color='k', linestyle='solid', label="Expected Amount of Flips", linewidth=1)

x_trial = np.arange(0, tests)
plt.title("Expected Coin Flips until " + str(h_in_row) + " Heads in a Row")
plt.xlabel("Successive Tests")
plt.ylabel("Flips per Test")
plt.plot(x_trial, df["Total Flips"], "k.", markersize=1.5, markevery=1, label="Flips Per Test")
plt.plot(x_trial, df["Average Flips"], color="r", linewidth=1, label="Average Flips")
plt.margins(x=0)
plt.legend()
plt.show()
