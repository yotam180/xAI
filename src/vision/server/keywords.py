#
#   Keyword processing utilities
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

import re
import os
import random

import cv2
import numpy as np

DATASET_DIR = "dataset/"

def get_id(text):
    """
    Encodes google search query or experssion to a keyword id
    For example: "Cute Dogs!" becomes "cute_dogs"
    """
    return "_".join(re.findall("\w+", text) or []).lower()

def exists(word):
    """
    Determines if a word exists in the dataset storage.
    """
    return os.path.exists(DATASET_DIR + get_id(word))

def collage(word):
    """
    Creates a beautiful collage of pictures of the same keyword
    """
    if not exists(word):
        return None
    
    w = get_id(word)
    f = sorted(os.listdir(os.path.abspath(DATASET_DIR + w)), key=lambda c: random.randint(1, 1e3))[:25]
    
    img = np.zeros((200, 200), np.uint8)

    for i, f in enumerate(f):
        c = cv2.imread(os.path.join(DATASET_DIR + w, f), cv2.IMREAD_GRAYSCALE)
        img[(i % 5) * 40 : (i % 5 + 1) * 40, (i // 5) * 40 : (i // 5 + 1) * 40] = c
    
    return img