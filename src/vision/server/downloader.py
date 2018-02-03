#
#   A module to download keywords requested by users.
#   Author: Yotam Salmon
#   Last Edited: 02/02/2018
#

# TODO: Organize imports
from google_images import GoogleSearch
from threading import Thread
import time
import urllib.request
import numpy as np
import cv2
import os

import task_scheduler as ts
from keywords import DATASET_DIR, get_id
from constants import IMG_SIZE

google = GoogleSearch()

_working = True

def run():
    work_thread = Thread(target=_work)
    work_thread.start()

def shutdown():
    _working = False

def _work():
    while _working:
        # Getting the next task we want to perform
        el = ts.get_next_download()

        # Continue if no task is waiting.
        if el == None:
            time.sleep(1)
            continue

        keyword = el["keyword"]
        kid = get_id(el["keyword"])

        # Checking if the keyword already exists
        if os.path.exists(DATASET_DIR + kid):
            ts.finished_download(el)
            continue

        print("Searching for " + keyword)
        
        # Sending the query to the google search module
        query = google.search(keyword, 300)
        urls = [x["tu"] for x in query if "tu" in x]
        el["downloaded"] = 0
        el["total"] = len(urls)

        # Creating the directory in dataset/
        os.makedirs(DATASET_DIR + kid)

        # And downloading all the files
        for i, img in enumerate(urls):
            obj = download(img)
            obj = cv2.resize(obj, (IMG_SIZE, IMG_SIZE))
            cv2.imwrite(DATASET_DIR + kid + "/" + str(i) + ".png", obj, [cv2.IMWRITE_PNG_COMPRESSION, 9])
            el["downloaded"] = i + 1

        # Calling the task callback to inform that we're done here
        ts.finished_download(el)

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