import os
import nLib
import cv2
import numpy as np
import time

# File structure
from storage import load_categories, save_categories, name_to_id

categories = load_categories()

models = {}


for id, cat in categories.items():
    print("Loading " + id)
    m = nLib.define_network_model(id)
    print("Created basic model")
    m.load(os.path.join(nLib.MODELS_DIR, id))
    models[id] = m
    print("Loaded " + id)

def classify(img):
    """
    Classifies a given image to most relevant categories
    """

    # 3-dimensioning the image
    if len(img.shape) < 3:
        img = img.reshape(img.shape[0], img.shape[1])
    
    # Converting to grayscale
    if img.shape[2] > 1:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    m = min(img.shape[0], img.shape[1])
    img = img[img.shape[0] // 2 - m // 2 : img.shape[0] // 2 + m // 2, img.shape[1] // 2 - m // 2 : img.shape[1] // 2 + m // 2]

    img = cv2.resize(img, (nLib.IMG_SIZE, nLib.IMG_SIZE))

    # return img

    res = []
    for id, net in models.items():
        r = net.predict(img.reshape(-1, nLib.IMG_SIZE, nLib.IMG_SIZE, 1))
        res.append((id, r[0][1] / np.sum(r)))
    
    return [i for i in sorted(res, key=lambda c: c[1], reverse=True) if i[1] > 1e-2]

def reload_model(cat_id):
    """
    Reloads a network model
    """
    m = nLib.define_network_model(cat_id)
    m.load(os.path.join(nLib.MODELS_DIR, cat_id))
    models[cat_id] = m

while True:
    url = input("Enter image path: ")
    print(classify(cv2.imread(url)))
