#
#   Keyword processing utilities
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

import re
import os

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