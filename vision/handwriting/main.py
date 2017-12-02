import mnist_loader
import nLib
import numpy as np

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = nLib.CNN([784, 30, 10], 3.0)
net.train(training_data, 30, 10, test_data, lambda p, w: np.argmax(p) == w)
net.save("network.net")