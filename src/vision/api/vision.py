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



def classify(image):
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
    pass