import neural_network
import numpy as np
import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

net = neural_network.Network([784, 30, 10])
net.gradient_descent(training_data, 30, 10, 4.0, test_data = test_data)