from random import random
import numpy as np
from matplotlib import pyplot as plt

h_in_row = input("How many heads in a row to test for? ")
counter = 0
total_count = 0
positions = []
heads = 0
total_flips = 0

while counter < int(h_in_row):
    prob = random()
    if 0 < prob < .5:  # flipped a heads
        counter += 1  # increase total heads by 1
        heads += 1  # head increase by 1
        total_flips += 1
    else:  # flipped a tails
        counter = 0  # reset counter for new iter
        total_flips += 1
        positions.append(heads)
        heads = 0
    if counter == int(h_in_row):
        positions.append(counter)

print("There were " + str(total_flips) + " total flips.")
print("There were " + str(len(positions)) + " total trials.")

x = np.arange(1, len(positions) + 1)
plt.title("Quarter flips")
plt.xlabel("Trials")
plt.ylabel("Heads Per Trial")
plt.plot(x, positions, 'k:')
plt.show()