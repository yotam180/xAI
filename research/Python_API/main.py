import nLib as nl
import numpy as np
from random import randint

net = nl.CNN([8, 10, 10, 1], 3)

rndarr = lambda: np.array([[randint(0, 1)] for x in range(8)])
pred = lambda c: np.array([[1 if c[2][0] == 0 and c[6][0] == 1 else 0]])
eval = lambda p, w: abs(w[0][0] - p[0][0]) < 0.5

training_data = []
test_data = []

for i in range(10000):
    x = rndarr()
    training_data.append((x, pred(x)))

for i in range(1000):
    x = rndarr()
    test_data.append((x, pred(x)))

print training_data