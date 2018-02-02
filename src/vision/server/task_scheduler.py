#
#   Task scheduling module for multithreading server
#   Author: Yotam
#   Last Edited: 02/02/2018
#

from random import randint
from threading import Lock

# These are the queues of net training and for dataset downloading
_create_net = []
_download_keyword = []

# For thread-safe queues
_cn = Lock()
_dl = Lock()

# These are the handlers that are publically exposed to get/set. 
# They are called once a task finishes.
on_net_created = None
on_keyword_downloaded = None

def download(keyword):
    """
    Adds a keyword to the download queue (downloads its images from Google too)
    Assigns a task to the google images module to search through.
    Returns the task id for checkups.
    """
    task_id = randint(1, 1e10)
    with _dl:
        _download_keyword.append({"keyword": keyword, "task_id": task_id})
    return task_id

def get_next_download():
    """
    Gets the next download task.
    """
    if len(_download_keyword) == 0:
        return None

    el = _download_keyword[0]
    with _dl:
        del _download_keyword[0]
    return el