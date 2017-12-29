import os
import json
import re

DATA_DIR = "data/"
IMAGE_DIR = "images/"
MODELS_DIR = "models/"
CHECKPOINTS_DIR = "checkpoints/"

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
