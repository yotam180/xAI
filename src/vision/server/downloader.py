#
#   A module to download keywords requested by users.
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

from google_images import GoogleSearch
from threading import Thread
import time
import urllib.request
import numpy as np
import cv2

import task_scheduler as ts

google = GoogleSearch()

_working = True

def run():
    work_thread = Thread(target=_work)
    work_thread.start()

def shutdown():
    _working = false

def _work():
    while _working:
        # Getting the next task we want to perform
        el = ts.get_next_download()

        # Continue if no task is waiting.
        if el == None:
            time.sleep(1)
            continue
        
        urls = None

def download(url):
    try:
        # Downloading the content
        req = urllib.request.urlopen(url)
        nparr = np.array(bytearray(req.read()))

        # Image-encoding the downloaded bytestream and returning the image
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)
        return img
    except:
        # Returning None upon exception.
        return None

def preview(img):
    """
    Opens a preview window for an image.
    """
    cv2.imshow("a", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()