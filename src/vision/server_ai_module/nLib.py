# Utils
import os
import shutil
import random
import re

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

# Image Processing
import cv2

# Math
import numpy as np

# Constants
from storage import DATA_DIR, MODELS_DIR, CHECKPOINTS_DIR, IMAGE_DIR

"""
Constants
"""
IMG_SIZE = 40
LEARNING_RATE = 1E-3


"""
Methods
"""

sess = T.Session()

def define_network_model(category_id):
    """
    Defines a network structure
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
    
    # Creating a model
    model = tflearn.DNN(net, tensorboard_dir="tensorboard", \
        best_checkpoint_path=os.path.join(CHECKPOINTS_DIR, category_id), \
        best_val_accuracy=0.7, session=sess)

    return model

def load_dataset(category):
    """
    Loads the dataset for a given category
    """

    res = []
    for im in [i for i in os.listdir(category["dir"]) if os.path.isfile(os.path.join(category["dir"], i))]:
        img = cv2.imread(os.path.join(category["dir"], im), cv2.IMREAD_GRAYSCALE).reshape(IMG_SIZE,IMG_SIZE,1)
        res.append((img, [0, 1]))
    for im in [i for i in os.listdir(category["negative"]) if os.path.isfile(os.path.join(category["negative"], i))]:
        img = cv2.imread(os.path.join(category["negative"], im), cv2.IMREAD_GRAYSCALE).reshape(IMG_SIZE,IMG_SIZE,1)
        res.append((img, [1, 0]))

    random.shuffle(res)
    
    return res

def create_model(category_id, category):
    """
    Creates a CNN model for a specific category based on its file dataset
    """

    # Creating the checkpoints directory, if doesn't exist
    if not os.path.exists(CHECKPOINTS_DIR):
        os.makedirs(CHECKPOINTS_DIR)

    # Loading the dataset
    dataset = load_dataset(category)

    test_data = dataset[:len(dataset) // 10]
    training_data = dataset[len(dataset) // 10 :]
    
    # Creating the network structure
    net = define_network_model(category_id)

    # Creating the dataset to be fed into the network
    X = np.array([i[0] for i in training_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    Y = [i[1] for i in training_data]

    test_X = np.array([i[0] for i in test_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    test_Y = [i[1] for i in test_data]
    print(test_Y)

    net.fit({"input": X}, {"targets": Y}, n_epoch=300, validation_set=({"input": test_X}, {"targets": test_Y}), show_metric=True, \
        snapshot_step=500, run_id=category_id + "_model")

    best_checkpoint = max([-1] + [int(x) for x in [(re.findall(category_id + "([0-9]+)\.meta", i) + [None])[0] for i in os.listdir(CHECKPOINTS_DIR)] if x])

    if best_checkpoint != -1:
        net.load(os.path.join(CHECKPOINTS_DIR, category_id + str(best_checkpoint)))

    net.save(os.path.join(MODELS_DIR, category_id))

    shutil.rmtree(CHECKPOINTS_DIR)

    return net
