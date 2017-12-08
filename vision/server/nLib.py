# Tensorflow
import tensorflow as T
T.reset_default_graph()

# TFLearn
import tflearn
from tflearn.data_utils import shuffle

# TFLearn Layers
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression

# TFLearn Data Preprocessing
from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

"""
Constants
"""
IMG_SIZE = 100
LEARNING_RATE = 1E-3

"""
Methods
"""

def define_network_model():
    """
    Defines a network structure
    """

    # Defining our image preprocessing
    proc = ImagePreprocessing()
    proc.add_featurewise_zero_center()
    proc.add_featurewise_stdnorm()

    # Defining image augmentation
    # We want to create a stilted wider dataset
    aug = ImageAugmentation()
    aug.add_random_flip_leftright()
    aug.add_random_blur(sigma_max=3.)
    aug.add_random_rotation(max_angle=20.)
    
    tf.reset_default_graph()

    # Input layer
    net = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name="input" \
        data_augmentation=aug, data_preprocessing=proc)

    # 2D Convolution layer
    net = conv_2d(net, 32, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 64, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 128, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 64, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 32, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # Hidden network layer
    net = fully_connected(net, 1024, activation='softmax')
    net = dropout(net, 0.8)

    # Output layer
    net = fully_connected(net, 2, activation='softmax')

    # Regression layer
    net = regression(net, optimizer='adam', learning_rate=LEARNING_RATE, \
        loss='categorical_crossentropy', name='targets')
    
    # Creating a model
    model = tflearn.DNN(net, tensorboard_dir="tensorboard")

    return model

def train(category):
    

"""
Action
"""