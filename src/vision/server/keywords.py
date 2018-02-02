#
#   Keyword processing utilities
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

import re

DATASET_DIR = "dataset/"

def get_id(text):
    """
    Encodes google search query or experssion to a keyword id
    For example: "Cute Dogs!" becomes "cute_dogs"
    """
    return "_".join(re.findall("\w+", text) or []).lower()