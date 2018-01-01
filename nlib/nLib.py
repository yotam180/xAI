# --- import statements ---

# For performing fast calculations
import numpy as np
from json import dumps, loads

# --- Constants ---

INVALID_INPUT_SIZE = "The size of the input did not match the size of the input layer"

class Math:
    """
    Math class for sigmoids and primes calculations
    """

    @staticmethod
    def sigmoid(z):
        """
        To compute the sigmoid factor of z
        """
        return 1.0 / (1.0 + np.exp(-z))

    @staticmethod
    def sigmoid_derivative(z):
        """
        To compute the first derivative of the sigmoid function for z
        """
        return Math.sigmoid(z) * (1 - Math.sigmoid(z))

    @staticmethod
    def quadratic_derivative(o, y):
        """
        Computes the first derivative of the quadratic cost function
        C(o)=1/2n*Sigma(oi-yi)**2
        """
        return o - y

class NetworkError(Exception):
    """
    Defines a neural network related error
    """
    pass

class InvalidInputError(NetworkError):
    """
    When the input size doesn't match the correct format or the size of the input layer of 
    the network.
    """
    pass

class Network(object):
    """
    Just for the correctness of the OOP model, we will have a base Network class and let
    the convolutional network inherit it. (We might want to add another type of network later)
    """
    pass

class CNN(Network):
    """
    The CNN class represents a fully connected convolutional neural network.
    It can predict outputs and learn from errors.
    """

    def save(self, file):
        """
        Saves the network model, with the biases and weights data, to a file.abs
        Parameters:
            file - the path/name of the file to update/create
        """
        with open(file, "w") as f:
            f.write(dumps({"learning_rate": self.learning_rate, "weights": [x.tolist() for x in self.weights], "biases": [x.tolist() for x in self.biases], "layers": self.sizes}))

    def load(self, file):
        """
        Loads a pre-saved neural network model from a file.
        Parameters:
            file - the path/name of the file to read from.

        The file must exist and be compatible with the JSON format. Otherwise an error will be raised.
        """
        with open(file, "r") as f:
            n = loads(f.read())
            self.learning_rate = n["learning_rate"]
            self.sizes = n["layers"]
            self.layers = len(self.sizes)
            self.weights = [np.array(x) for x in n["weights"]]
            self.biases = [np.array(x) for x in n["biases"]]

    def __init__(self, sizes, learning_rate = 1.0):
        """
        Initializing a new neural network with biases and weights as given in the parameters
        Parameters:
            layers - the array representing the layers sizes
            learning_rate - the learning rate of the network
        """
        
        if type(sizes) == type(""):
            self.load(sizes)
            return

        """
        The count of layers in the network (layers = input + hidden + output)
        """
        self.layers = len(sizes)

        """
        The sizes of the layers
        """
        self.sizes = [s for s in sizes] 
        # Creating a copy of the parameter instead of using it.

        """
        Randomizing the biases for the network
        """
        self.biases = [np.random.randn(n, 1) for n in self.sizes[1:]]
        # Explanation:
        # np.random.randn(n, 1) - a vector (1D matrix) that will be represented in NumPy as a 3D matrix
        #   for the conveniency of multiplying
        # self.sizes[1:] - we only want to make biases starting from the second layer (input layer doesn't make modification)

        """
        Randomizing the weights for the network
        """
        self.weights = [np.random.randn(m,n) for n, m in zip(self.sizes[:-1], self.sizes[1:])]
        # Explanation:
        # np.random.randn(m, n) - we use the inversed sizes
        #   For example: from a layer of 6 neurons to a layer of 10 neurons, the weights matrix
        #   will be a 10,6 matrix.
        #   Why? Because we want to evaluate weights(l) * activations(l-1) and it's possible easily
        #   When weights is (n, m) and activations are (m, 1) (outputs vector (n, 1))
        # zip(self.sizes[:-1], self.sizes[1:])
        #   Creates a connecting array for every layer L and layer L+1

        self.learning_rate = learning_rate

    def predict(self, x):
        """
        Predict will take a vector of inputs and returns the vector of outputs
        from the output layer.
        Parameters -
            x - the vector of inputs. Recommended to be a 2D numpy array shaped (n, 1)
                (n being the size of the input layer). Can also be a 1D numpy array shaped
                (n) or a Python list with length n.
        """

        if "'list'" in str(type(x)):
            # Checking for invlid length
            if len(x) != self.sizes[0]:
                raise InvalidInputError(INVALID_INPUT_SIZE)

            # Casting it to a numpy array
            x = np.array([[i] for i in x])
        
        if "'numpy.ndarray'" in str(type(x)):
            # Checking for size suitability
            if x.shape[0] != self.sizes[0]:
                raise InvalidInputError(INVALID_INPUT_SIZE)
            
            if len(x.shape) == 1:
                # Buffing the 1 dimensional array to 2D matrix of (n, 1)
                x = np.array([[i] for i in x])

            if len(x.shape) > 2:
                raise InvalidInputError(INVALID_INPUT_SIZE)

        # First layer activation
        a = x

        for w, b in zip(self.weights, self.biases):
            # Calculating the linear output of the layer
            z = np.dot(w, a) + b

            # Applying the sigmoid function to normalize the linear output
            a = Math.sigmoid(z)

        return a
    
    def back_propagate(self, x, y):
        """
        Performs a back propagation algorithm over the network and splits
        the blame across all the neurons.
        Parameters:
            x - the given input
            y - the optimal output for the given input
        Return value:
            tuple - 
                [0] - the list of biases blame for every layer
                [1] - the list of weights blame for every layer
        """

        # Constructing empty (zero'd) matrices for storing the aggregation of error
        n_biases = [np.zeros(b.shape) for b in self.biases]
        n_weights = [np.zeros(w.shape) for w in self.weights]

        # First activation
        a = x

        # Activations history (over the layers of the network)
        activations = [x]

        # For storing the Z values of the neurons (before applying the sigmoid function)
        zs = []

        # Feed-forwarding through the network
        for w, b in zip(self.weights, self.biases):
            z = np.dot(w, a) + b
            zs.append(z)
            a = Math.sigmoid(z)
            activations.append(a)
        
        L = self.layers

        # Delta - the quadratic cost derivative of the last activation, compared to the optimal output.
        d = Math.quadratic_derivative(activations[L - 1], y) * Math.sigmoid_derivative(zs[L - 2])

        # Updating the sum of the biases and weights
        n_biases[L - 2] = d
        n_weights[L - 2] = np.dot(d, activations[L - 2].transpose())

        for l in range(L - 1, 1, -1):
            # Computing the sigmoid derivative of the partial activation value
            z = zs[l - 2]
            sd = Math.sigmoid_derivative(z)

            # Back propagating one layer back
            d = np.dot(self.weights[l - 1].transpose(), d) * sd

            # Updating the biases and weights for that layer
            n_biases[l - 2] = d
            n_weights[l - 2] = np.dot(d, activations[l - 2].transpose())

        return n_biases, n_weights

    def evaluate(self, test_data, predicate):
        """
        Using a given predicate, predicts and evaluates the rate of success
        Parameters:
            test_data - the data to test against
            predicate - a method that will return true upon a successful predict, and false otherwise
        """
        return sum([
            int(predicate(self.predict(x), y)) for x, y in test_data
        ])

    def mini_batch(self, batch):
        """
        Performs SGD for a mini-batch of data and updates the network parameters
        according to.
        """

        # Constructing empty (zero'd) matrices for storing the aggregation of error
        n_biases = [np.zeros(b.shape) for b in self.biases]
        n_weights = [np.zeros(w.shape) for w in self.weights]

        for x, y in batch:

            # Computing the delta values for the weights and biases
            d_biases, d_weights = self.back_propagate(x, y)

            # Adding the delta values to the aggregation
            n_biases = [nb + delta_nb for nb, delta_nb in zip(n_biases, d_biases)]
            n_weights = [nw + delta_nw for nw, delta_nw in zip(n_weights, d_weights)]

        self.weights = [w - self.learning_rate * (delta_w / len(batch)) for w, delta_w in zip(self.weights, d_weights)]
        self.biases = [b - self.learning_rate * (delta_b / len(batch)) for b, delta_b in zip(self.biases, d_biases)]
    
    def train(self, training_data, epochs, mini_batch_size, test_data = None, pred = None):
        """
        Performs deep learning over the network.
        Parameters:
            training_data - a list of tuples to learn from (first element - x, second element - y)
            epochs - number of trining epochs.
            mini_batch_size - the size of the mini batches to split the data to. 
            test_data - the test data to evaluate
        """
        if test_data:
            tests = len(test_data)
        
        n = len(training_data)

        max_eval = 0
        mw = None
        mb = None
        me = None

        for j in range(epochs):

            # Shuffling the training data
            np.random.shuffle(training_data)

            # Dividing the training data to mini batches
            mini_batches = [training_data[k:k+mini_batch_size] for k in range(0, n, mini_batch_size)]
            
            # Iterating over all mini batches
            for b in mini_batches:
                self.mini_batch(b)

            if test_data:
                ev = self.evaluate(test_data, pred)
                print "Epoch %d/%d - %f success" % (j + 1, epochs, ev * 100.0 / len(test_data))
                if (ev >= max_eval):
                    max_eval = ev
                    mw = self.weights
                    mb = self.biases
                    me = j
            else:
                print "Epoch %d/%d" % (j + 1, epochs)
        
        print "================="
        print "Selecting epoch %d (success rate %f)" % (me + 1, max_eval * 100.0 / len(test_data))
        self.weights = mw
        self.biases = mb
        print "Epoch %d/%d - %f success" % (me + 1, epochs, self.evaluate(test_data, pred) * 100.0 / len(test_data))