from random import random
import numpy as np
from matplotlib import pyplot as plt

customers = 0

p = input("What is probability to move forward? ")
p = float(p)
# q = input("What is the probability of the first customer leaving? ")
# q = float(q)

forward = p
backwards = 1-p
# same = (p*q)+((1-q)*(1-p))

time = input("How many time steps to run? ")
time = int(time)
totaltime = time

positions = [customers]

while time > 1:
    prob = random()
    if 0 < prob <= forward:
        customers += 1
    else:
        customers -= 1
    # elif forward < prob <= (forward + same):
    #     customers = customers
    # elif (forward + same) < prob <= 1:
    #     customers -= 1
    # if customers == -1:
    #     customers = 0
    time -= 1
    positions.append(customers)

print("After " + str(totaltime) + " time steps, you are at " + str(customers) + ".")

x = np.arange(0, totaltime)
plt.title("Number")
plt.xlabel("Time")
plt.ylabel("Time Line")
plt.plot(x, positions, 'r-')
plt.show()