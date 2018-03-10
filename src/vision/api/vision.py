#
#   The Python v3.5 release API of xAI vision.
#   Yotam Salmon 2018 (C) All rights reserved.
#   Last stable version: 0.0.1
#

numpy_exists = True
try:
    import numpy as np
except:
    numpy_exists = False

import requests
import base64
import json

__server = "http://localhost:8080/v?id="

def __hexdump_bytes(b):
    """
    Encodes bytes object into base64 string.
    """
    return str(base64.b64encode(b), "ascii")

def __hex_ndarray(image):
    """
    Transforms an ndarray to a base64 string that is sendable to xAI.
    """
    image = image.reshape((-1))
    return __hexdump_bytes(bytes(image))

def __hex_file(image):
    """
    Reads a file and converts it to a base64 string that is sendabe to xAI.
    """
    cont = image.read()
    return __hexdump_bytes(cont)

def __classify(hx, cid):
    """
    Sends a base64 payload to xAI and returns the result.
    """
    r = requests.post(__server, data=json.dumps({"c": cid, "i": hx}))
    return r.json()

def classify(image, classifier_id):
    """
    Classifies an image using one of xAI's convolutional neural networks.
    
    Parameters:
        image:
            -> str - the location of the image file to classify.
            -> file - the file to classify.
            -> np.array - the image as a numpy array (from cv2 or PIL). 
        The image is encoded into base64 and then sent to xAI servers. 
    
    Return value:
        dictionary - the result returned from the xAI server.
    """

    if numpy_exists and type(image) == np.ndarray:
        payload = __hex_ndarray(image)
    elif type(image) == str:
        payload = __hex_file(open(image, "rb"))
    else:
        payload = __hex_file(image)

    return __classify(payload, classifier_id)