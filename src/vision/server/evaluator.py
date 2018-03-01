#
#   Classifier evaluation module
#   Author: Yotam Salmon
#   Last Edited: 28/02/2018
#

import nLib

import cv2
import numpy as np

classifiers = {}

def process_image(img):
    """
    Converts an arbitary image to a matrix that can be fed into a classifier.
    """
    
    # Making the image 3D
    if len(img.shape) < 3:
        img = img.reshape(img.shape[0], img.shape[1], 1)

    # Grayscaling the image
    if img.shape[2] > 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Cutting the center square
    m = min(img.shape[0], img.shape[1])
    img = img[img.shape[0] // 2 - m // 2 : img.shape[0] // 2 + m // 2, img.shape[1] // 2 - m // 2 : img.shape[1] // 2 + m // 2]

    # Resizing
    img = cv2.resize(img, (nLib.IMG_SIZE, nLib.IMG_SIZE))

    return img

def classify_image(img, classifier_name):
    """
    Classifying an image
    """
    global classifiers

    try:
        X = process_image(img)
    except:
        return False, "Error while trying to process the image"
    
    if classifier_name in classifiers.keys():
        C = classifiers[classifier_name]
    else:
        try:
            C = nLib.load_classifier(classifier_name)
            classifiers[classifier_name] = C
        except:
            return False, "Error while trying to load the classifier"

    try:
        Y = C.predict(X.reshape(-1, nLib.IMG_SIZE, nLib.IMG_SIZE, 1))
    except:
        return False, "Error while trying to analyze the image"

    return True, Y[0][1] / np.sum(Y)