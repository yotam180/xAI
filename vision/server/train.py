"""
Modules and inclusions
"""

# Utility modules
import os
import json
import re
from random import shuffle, randint

# Image processing modules
import numpy as np 
import cv2

# Machine learning modules
import nLib

# Data mining modules
from google_images import GoogleSearch

# Connectivity modules
from socket import socket
import urllib

# Logging modules
import logger

"""
Constants
"""
DATA_DIR = "data/"
IMAGE_DIR = "images/"
MODELS_DIR = "models/"

"""
Methods
"""

def load_categories():
    """
    Loads predefined categoies
    """
    logger.log(os.path.join(DATA_DIR, "dataset.json"))
    with open(os.path.join(DATA_DIR, "dataset.json"), "r") as f:
        return json.loads(f.read())


def name_to_id(category_name):
    """
    Converts a category name to its perspective ID
    """
    return "_".join(re.findall("\w+", category_name) or []).lower()


def import_image(url):
    """
    Downloads an image from a URL
    """
    req = urllib.urlopen(url)
    nparr = np.array(bytearray(req.read()))
    img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (nLib.IMG_SIZE, nLib.IMG_SIZE))
    return img


def create_dataset(category_name):
    """
    Creates and saves a dataset to a folder
    """
    
    category_id = name_to_id(category_name)

    # Checking for duplicates in the category name:
    if category_id in categories.keys() or not category_id:
        return False

    # Searching query on Google
    src = google.search(category_name, 1)

    # And iterating through results
    for pic in src:
        img = import_image(pic["tu"])

"""
Initializations
"""

logger.log("Hello World")

# We'll open a new GoogleSearch instance
google = GoogleSearch()

# And initialize all the categories
categories = load_categories()

"""
Action
"""

create_dataset("Car")