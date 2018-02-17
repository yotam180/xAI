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
import urllib.request

# Logging modules
import logger

# Constant imports
from storage import DATA_DIR, IMAGE_DIR, MODELS_DIR, CHECKPOINTS_DIR

# File structure
from storage import load_categories, save_categories, name_to_id

"""
Constants
"""


"""
Methods
"""

def import_image(url):
    """
    Downloads an image from a URL
    """
    try:
        # Downloading the image from the remote
        req = urllib.request.urlopen(url)
        nparr = np.array(bytearray(req.read()))
        
        # Formatting the image as we wish it to be
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (nLib.IMG_SIZE, nLib.IMG_SIZE))
        return True, img # Success
    except:
        return False, None # Failure


def create_dataset(category_name, negatives):
    """
    Creates and saves a dataset to a folder
    """
    global categories
    
    category_id = name_to_id(category_name)

    # Checking for duplicates in the category name:
    if category_id in categories.keys() or not category_id:
        return False

    # Searching query on Google
    src = google.search(category_name, 500)

    # Creating the folders for storing the training data
    if not os.path.exists(os.path.join(IMAGE_DIR, category_id)):
        os.makedirs(os.path.join(IMAGE_DIR, category_id))
    if not os.path.exists(os.path.join(IMAGE_DIR, category_id, "negative")):
        os.makedirs(os.path.join(IMAGE_DIR, category_id, "negative"))

    # And iterating through results
    for i, pic in enumerate(src):
        success, img = import_image(pic["tu"])
        if not success:
            continue # If the download has failed
            
        # Saving the image to the category folder
        cv2.imwrite(os.path.join(IMAGE_DIR, category_id, str(i) + ".png"), img)

    for cat in negatives:
        src2 = google.search(cat, len(src) // len(negatives))
        for i, pic in enumerate(src2[:len(src) // len(negatives)]):
            success, img = import_image(pic["tu"])
            if not success:
                continue
            cv2.imwrite(os.path.join(IMAGE_DIR, category_id, "negative", str(randint(1, 100000)) + ".png"), img)


    # Refreshing the categories list
    categories = load_categories()
    categories[category_id] = {
        "name": category_name, 
        "dir": os.path.join(IMAGE_DIR, category_id), 
        "negative": os.path.join(IMAGE_DIR, category_id, "negative")
    }
    save_categories(categories)

    # Returning true upon success
    return True
        

"""
Initializations
"""

# We'll open a new GoogleSearch instance
google = GoogleSearch()

# And initialize all the categories
categories = load_categories()

"""
Action
"""

def train_for(yes, nos):
    cid = name_to_id(yes)
    #if cid in categories.keys():
    #    logger.log("Category " + cid + " already exists!")
    #    return False
    
    #logger.log("Creating dataset for " + yes)
    #create_dataset(yes, nos)

    logger.log("Creating model for " + yes)
    net = nLib.create_model(cid, categories[cid])
    net.save(os.path.join(MODELS_DIR, cid))

# train_for("Car", ["Dog", "Snake", "Tree", "Cat", "Train", "City"])
train_for("Snake", ["Dog", "Cat", "Tree", "Car", "Train", "City"])
train_for("Table", ["Dog", "Snake", "Tree", "Car", "Train", "City", "Cat", "Lizard"])