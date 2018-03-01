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
import re
import shutil
import time

# Constants and settings
from constants import IMG_SIZE, DEBUG, CLASSIFIER_DIRECTORY

# Defining our own constants
LEARNING_RATE = 1e-3
CHECKPOINT_DIR = "checkpoint"

POSITIVE_TUP = [0, 1]
NEGATIVE_TUP = [1, 0]

def define_network():
    """
    Used for creating networks.
    Constructs the basic structure of a network
    """

    # Defining image augmentation
    # We want to create a stilted wider dataset
    aug = ImageAugmentation()
    aug.add_random_flip_leftright()
    aug.add_random_blur(sigma_max=3.)
    aug.add_random_rotation(max_angle=20.)
    
    T.reset_default_graph()

    # Input layer
    net = input_data(shape=[None, IMG_SIZE, IMG_SIZE, 1], name="input", \
        data_augmentation=aug)
    
    # 2D Convolution layer
    net = conv_2d(net, 32, 5, activation='relu')
    net = max_pool_2d(net, 3)

    # 2D Convolution layer
    net = conv_2d(net, 64, 5, activation='relu')
    net = max_pool_2d(net, 3)

    # 2D Convolution layer
    net = conv_2d(net, 32, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 64, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # 2D Convolution layer
    net = conv_2d(net, 32, 5, activation='relu')
    net = max_pool_2d(net, 5)

    # Hidden network layer
    net = fully_connected(net, 512, activation='relu')
    net = dropout(net, 0.8)

    # Output layer
    net = fully_connected(net, 2, activation='softmax')

    # Regression layer
    net = regression(net, optimizer='adam', learning_rate=LEARNING_RATE, \
        loss='categorical_crossentropy', name='targets')
    
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
        best_val_accuracy=0.5
    )

def define_evaluation_model():
    """
    Defines a model for evaluation. Does not dictate checkpoint dir.
    """
    global sess

    return tflearn.DNN(
        define_network()
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

def train_classifier(classifier_id, dataset):
    """
    Trains a classifier based on a given dataset.
    Parameters:
        classifier_id - the id of the classifier (string)
        dataset - the result of calling load_dataset on some keywords.
    """
    # Checking that the checkpoints directory doesn't exist, then creating it.
    # We really want to clean the folder CHECKPOINTS_DIR before we start training
    # so we don't accidentaly take another model's checkpoints to our classifier.
    if os.path.exists(CHECKPOINT_DIR):
        shutil.rmtree(CHECKPOINT_DIR)
    time.sleep(0.5)
    os.makedirs(CHECKPOINT_DIR)

    # Splitting to training and test data.
    test_data = dataset[:len(dataset) * 3 // 10]
    training_data = dataset[len(dataset) * 3 // 10:]

    # Creating our model to train
    net = define_training_model(classifier_id)

    # Processing the dataset
    X = np.array([i[0] for i in training_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    Y = [i[1] for i in training_data]

    test_X = np.array([i[0] for i in test_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    test_Y = [i[1] for i in test_data]

    # Doing the AI "magic" to train our model with the dataset we just created
    net.fit(
        {"input": X}, 
        {"targets": Y}, 
        n_epoch=2 if DEBUG else 300, 
        validation_set=(
            {"input": test_X},
            {"targets": test_Y}
        ),
        show_metric=True,
        snapshot_step=500,
        run_id=classifier_id + "_model"
    )

    # Retrieving the best checkpoint we have hit during the training process
    # So we are sure to take the best network out of the whole thing
    best_checkpoint = max(
        [-1] + [int(x) for x in [(re.findall(classifier_id + "([0-9]+)\.meta", i) + [None])[0] for i in os.listdir(CHECKPOINT_DIR)] if x]
    )
    if best_checkpoint != -1:
        net.load(os.path.join(CHECKPOINT_DIR, classifier_id + str(best_checkpoint)))

    # Removing the checkpoint directory
    shutil.rmtree(CHECKPOINT_DIR)

    # And returning the result
    return net

def load_classifier(classifier_name):
    """
    Loads a pre-trained classifier model from ckpt files under CLASSIFIER_DIRECTORY
    Parameters:
        classifier name (not database ID)
    """
    net = define_evaluation_model()
    net.load(os.path.join(CLASSIFIER_DIRECTORY, classifier_name))
    return net