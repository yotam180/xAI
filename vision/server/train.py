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
from nLib import DATA_DIR, IMAGE_DIR, MODELS_DIR

"""
Constants
"""


"""
Methods
"""

def load_categories():
    """
    Loads predefined categoies
    """
    with open(os.path.join(DATA_DIR, "dataset.json"), "r") as f:
        return json.loads(f.read())


def save_categories(c):
    """
    Saves predefined categories
    """
    with open(os.path.join(DATA_DIR, "dataset.json"), "w") as f:
        f.write(json.dumps(c))


def name_to_id(category_name):
    """
    Converts a category name to its perspective ID
    """
    return "_".join(re.findall("\w+", category_name) or []).lower()


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

# create_dataset("Snake", ["Cat", "Dot", "Truck", "House", "Airplane", "City", "Forest", "Person"])
net = nLib.create_model("dog", categories["dog"])
net.save(os.path.join(MODELS_DIR, "dog"))