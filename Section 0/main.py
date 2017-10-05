import neural_network
import numpy as np

net = neural_network.Network([3, 5, 3])
result = net.feed_forward(np.array(
    [[0.5], [1], [0]]
    ))
print result