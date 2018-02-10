#
#   The module in charge of addressing TensorFlow and training networks.
#   Author: Yotam Salmon
#   Last Edited: 10/02/2018
#

# Importing TensorFlow
import tensorflow as T
T.reset_default_graph()

# And tfLearn
import tflearn
from tflearn.data_utils import shuffle

from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, fully_connected, dropout
from tflearn.layers.estimator import regression

from tflearn.data_preprocessing import ImagePreprocessing
from tflearn.data_augmentation import ImageAugmentation

# OpenCV for image manipulations
import cv2

# Numpy for mathematical operations
import numpy as np

# Utilites
import os
import random

# Constants and settings
from constants import IMG_SIZE

# Defining our own constants
LEARNING_RATE = 1e-3
CHECKPOINT_DIR = "checkpoint"

POSITIVE_TUP = [0, 1]
NEGATIVE_TUP = [1, 0]

# Creating a TensorFlow session
sess = T.Session()

def define_network():
    """
    Used for creating networks.
    Constructs the basic structure of a network
    """

    # Augmentation for images
    aug = ImageAugmentation()
    aug.add_random_flip_leftright()
    aug.add_random_blur(sigma_max=3.)
    aug.add_random_rotation(max_angle=40.)

    T.reset_default_graph()

    # First input layer
    net = input_data(
        shape=[None, IMG_SIZE, IMG_SIZE, 1],
        name="input",
        data_augmentation=aug
    )

    # 2D convolution layer
    net = conv_2d(
        net,
        32,
        5,
        activation='relu'
    )

    # 2D convolution layer
    net = conv_2d(
        net,
        64,
        5,
        activation='relu'
    )

    # 2D convolution layer
    net = conv_2d(
        net,
        32,
        5,
        activation='relu'
    )

    # 2D convolution layer
    net = conv_2d(
        net,
        64,
        5,
        activation='relu'
    )

    # 2D convolution layer
    net = conv_2d(
        net,
        32,
        5,
        activation='relu'
    )

    # Hidden fully-connected layer
    net = fully_connected(
        net,
        512,
        activation='relu'
    )
    
    # Dropping out some nodes to prevent overfitting
    net = dropout(
        net,
        0.8
    )

    # Hidden fully-connected layer
    net = fully_connected(
        2,
        activation='softmax'
    )

    # Regression
    net = regression(
        net,
        optimizer='adam',
        learning_rate=LEARNING_RATE,
        loss='categorical_crossentropy',
        name='targets'
    )

    # The network was successfully created
    return net

def define_training_model(ckpt_id):
    """
    Defines a model for training (dictates the model to write checkpoints)
    Parameters:
        ckpt_id - the dataset id of the model
    Return value:
        The created model.
    """
    global sess

    return tflearn.DNN(
        define_network(),
        tensorboard_dir="/tensorboard/",
        best_checkpoint_path=os.path.join(CHECKPOINT_DIR, ckpt_id),
        best_val_accuracy=0.5,
        session=sess
    )

def define_evaluation_model():
    """
    Defines a model for evaluation. Does not dictate checkpoint dir.
    """
    global sess

    return tflearn.DNN(
        define_network(),
        session=sess
    )

def load_dataset(positives, negatives):
    """
    Loads the positive and negative words and returns a training set.
    Parameters:
        positives - list of positive keyword ids to load.
        negatives - list of negative keyword ids to load.
    Notes - the words should already be downloaded to the dataset folder. This method will ignore words that are not present there.abs
    Return value:
        The list of arrays of something... The training data, simply.
    """

    res = []

    for word in positives:
        if os.path.exists(os.path.join("dataset", word)):
            for pic in os.listdir(os.path.join("dataset", word)):
                path = os.path.join("dataset", word, pic)
                
                # Reshaping our image to 3D although it is just grayscale
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE).reshape(IMG_SIZE, IMG_SIZE, 1)

                # And appending it to our result list
                res.append([img, POSITIVE_TUP])

    for word in negatives:
        if os.path.exists(os.path.join("dataset", word)):
            for pic in os.listdir(os.path.join("dataset", word)):
                path = os.path.join("dataset", word, pic)
                
                # Reshaping our image to 3D although it is just grayscale
                img = cv2.imread(path, cv2.IMREAD_GRAYSCALE).reshape(IMG_SIZE, IMG_SIZE, 1)

                # And appending it to our result list
                res.append([img, NEGATIVE_TUP])

    # Shuffling our dataset
    random.shuffle(res)

    return res