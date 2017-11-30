import nLib as nl
import numpy as np
from random import randint

"""
Creating our new CNN (Convolutional Neural Network)
4 layers:
    Input layer of size 8
    Hidden layer of size 15
    Hidden layer of size 10
    Output layer of size 1
Learning rate is 4.0
"""
net = nl.CNN([8, 15, 10, 1], 4.0)

# For randomizing arrays
rndarr = lambda: np.array([[randint(0, 1)] for x in range(8)])
# For creating the desired output (defining a logical rule)
pred = lambda c: np.array([[1 if c[2][0] == 0 and c[6][0] == 1 else 0]])
# For evaluating a predicted output against a known output
eval = lambda p, w: abs(w[0][0] - p[0][0]) < 0.5

training_data = []
test_data = []

# Creating our training data
for i in range(10000):
    x = rndarr()
    training_data.append((x, pred(x)))

# Creating our test data
for i in range(1000):
    x = rndarr()
    test_data.append((x, pred(x)))

# training our network
net.train(training_data, 100, 20, test_data, eval)