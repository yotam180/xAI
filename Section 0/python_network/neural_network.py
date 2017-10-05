import numpy as np

#
# In this file we'll define our neural network class
#
# Author:   Yotam Salmon
# Date:     05/10/17
#

class Network(object):
    """ Defines a neural network. """
    
    def __init__(self, layers):
        """ Constructs a new Network object with random weights and biases. """
        
        # Setting the number of layers the network has
        # For example, [5, 3, 4] signifies 3 layers. First has 5 neurons, second has 3 and last has 4.
        self.num_layers = len(layers)

        # And keeping track of the sizes of the layers, too (not only their count)
        self.sizes = layers

        # Creating biases for each layer (each layer has sizes[n] biases)
        self.biases = [np.random.randn(y, 1) for y in self.sizes[1:]]

        # Creating weights for each connection layer 
        # (every 2 adjacent layers have n*m connections, n=size of prev layer, m=size of next layer)
        # The matrix weights[...] itself will be of dimensions m*n (and not n*m)
        self.weights = [np.random.randn(m, n) for n,m in zip(self.sizes[:-1], self.sizes[1:])]

    def feed_forward(self, a):
        """ Simulates a data passing through the network. `a` is an array with the size of the input layer """
        
        # Iterating through all layers of the network
        for w, b in zip(self.weights, self.biases):
            # According to the equation a'=sig(wa+b)
            a = sigmoid(np.dot(w, a) + b)

        # In this point, a contains the result of the final layer.
        return a

    def gradient_descent(self, training_data, epochs, mini_batch_size, learning_rate, test_data = None):
        """ Performs stochastic gradient descent for a given training data. """

        # Setting up our constants
        if test_data:
            tests_num = len(test_data)
        n = len(training_data)

        for j in range(epochs):

            # Shuffling the training data
            np.random.shuffle(training_data)

            # Dividing our training data to mini batches of size `mini_batch_size`
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, len(training_data), mini_batch_size)]

            # Applying gradient descent for each of the batches
            for batch in mini_batches:
                self.update_mini_batch(batch, learning_rate)
            
            if test_data:
                print "Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), tests_num
                )
            else:
                print "Epoch", j

    def update_mini_batch(self, batch, learning_rate):
        """ Performs gradient descent based on a batch of data and a learning rate. """
        
        nb = [np.zeros(b.shape) for b in self.biases]
        nw = [np.zeros(w.shape) for w in self.weights]

        for x, y in batch:
            
            # Computing the delta values for the weights and biases
            delta_nb, delta_nw = self.backprop(x, y)

            # Adding those delta values to the nb and nw matrixes
            nb = [_nb + _dnb for _nb, _dnb in zip(nb, delta_nb)] # TODO : check the contents of delta_nb against nb and see if we can do it using numpy more elegantly
            nw = [_nw + _dnw for _nw, _dnw in zip(nw, delta_nw)]

        # Updating the weights and biases of the network itself
        self.weights = [w - learning_rate * (dw / len(batch)) for w, dw in zip(self.weights, nw)]
        self.biases =  [b - learning_rate * (db / len(batch)) for b, db in zip(self.biases , nb)]


    def evaluate(self, test_data):
        """ Evaluates the test data and scores results. """

        # Get the result digit from the network and the actual digit from the test data
        test_results = [
            (np.argmax(self.feed_forward(x)), y) for (x, y) in test_data
        ]

        # Count how many of the results are correct
        return sum(
            [int(x == y) for (x, y) in test_results]
        )


    def cost_derivative(self, output_activations, y):
        """ Does something with the derivative of the cost (?) """

        # Dafuq is that?
        return (output_activations - y)

    def backprop(self, x, y): ## TODO WRITE BY MYSELF TODO

        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x] # list to store all the activations, layer by layer
        zs = [] # list to store all the z vectors, layer by layer
        for b, w in zip(self.biases, self.weights):
            z = np.dot(w, activation)+b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * \
            sigmoid_prime(zs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())
        # Note that the variable l in the loop below is used a little
        # differently to the notation in Chapter 2 of the book.  Here,
        # l = 1 means the last layer of neurons, l = 2 is the
        # second-last layer, and so on.  It's a renumbering of the
        # scheme in the book, used here to take advantage of the fact
        # that Python can use negative indices in lists.
        for l in xrange(2, self.num_layers):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        return (nabla_b, nabla_w)

### Helper functions ###

def sigmoid(z):
    """ To compute a sigmoid function f(x)=1/(1+exp(-x)) of the input z """
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_prime(z):
    """ Computes the derivative of the sigmoid function. """
    return sigmoid(z) * (1 - sigmoid(z))