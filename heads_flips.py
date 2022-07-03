from random import random
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.DataFrame(columns=["Total Flips", "Total Trials", "Average Flips"])

h_in_row = int(input("How many heads in a row to test for? "))
tests = int(input("How many tests? "))
expected = 2 ** (h_in_row + 1) - 2

total_count = 0

'''
This method runs one trial, that is it will calculate how 
many coin flips required until there are X heads in a row.
:param head_in_row: How many heads in a row the trial will test for
:return Returns a new row in the df with the amount of flips required, trials needed, and new average
'''


def trial(head_in_row):
    counter = 0
    heads = 0
    trial.total_flips = 0
    trial.positions = []
    while counter < int(head_in_row):
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
        if counter == int(head_in_row):
            trial.positions.append(counter)
            df.loc[len(df.index)] = [trial.total_flips, len(trial.positions), df["Total Flips"].mean()]


# Upload all trials into the dataframe
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


fig = px.scatter(df, x=df.index, y="Total Flips", title="Expected Coin Flips until "
                                                        + str(h_in_row) + " Heads in a Row",
                 labels={"index": "Trial", "Total Flips": "Flips per Trial"}, animation_frame=df.index,
                 animation_group="Total Flips")


fig.update_traces(marker_size=5)
fig.update_yaxes(automargin=True)
fig.add_trace(go.Scatter(x=df.index, y=df["Average Flips"], name="Moving Average"))
fig.add_hline(y=expected)
fig.show()

