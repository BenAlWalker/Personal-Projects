import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# read in csv file
data = pd.read_csv("heart.csv")

A = data[['Age', 'MaxHR']]

A = A[np.all(A != 0, axis=1)]

matrix = np.array(A.values, 'float')
X = matrix[:, 0]
y = matrix[:, 1]

plt.plot(X, y, 'b.', markersize=1)
plt.ylabel('MaxHR')
plt.xlabel('Age')
plt.title('Age to Max HR')
plt.margins(x=0)
plt.grid(which='major')

a, b = np.polyfit(X, y, 1)
plt.plot(X, a * X + b, color='black')
plt.text(62, 190, 'y = ' + str(round(b, 2)) + ' ' + str(round(a, 2)) + 'x', size=10)
plt.show()
