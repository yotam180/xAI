#
#   Task scheduling module for multithreading server
#   Author: Yotam
#   Last Edited: 17/02/2018
#

from random import randint
from threading import Lock

# These are the queues of net training and for dataset downloading
_create_net = []
_download_keyword = []

_current_keyword = None
_current_training = None

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
    global _dl
    global _download_keyword
    task_id = randint(1, 1e10)
    with _dl:
        _download_keyword.append({"keyword": keyword, "task_id": task_id})
    return task_id

def train(dataset_id, classifier_id):
    """
    Adds a dataset to the training queue.
    Assigns a task to the TensorFlow trainer module to train.
    Returns the task id for checkups.
    """
    global _cn
    global _create_net
    task_id = randint(1, 1e10)
    with _cn:
        _create_net.append({"dataset_id": dataset_id, "classifier_id": classifier_id, "task_id": task_id})
    return task_id

def get_next_download():
    """
    Gets the next download task.
    """
    global _current_keyword
    global _dl
    if len(_download_keyword) == 0:
        return None

    el = _download_keyword[0]
    with _dl:
        del _download_keyword[0]
    
    _current_keyword = el
    return el

def get_next_training_candidate():
    """
    Gets the next training task.
    """
    global _current_training
    global _cn
    if len(_create_net) == 0:
        return None

    el = _create_net[0]
    with _cn:
        del _create_net[0]
    
    _current_training = el
    return el


def finished_download(el):
    """
    Removes the current downloading task and calls the handler for finishing.
    Should be called by the worker.
    """
    global _current_keyword
    if el["task_id"] == _current_keyword["task_id"]:
        _current_keyword = None
        if (on_keyword_downloaded):
            on_keyword_downloaded(el)

def finished_training(el):
    """
    Removes the current training task and calls the handler for finishing.
    Should be called by the worker (trainer). 
    """
    global _current_training
    if el["task_id"] == _current_training["task_id"]:
        _current_training = None
        if (on_net_created):
            on_net_created(el)


def get_download_status(task_id):
    global _current_keyword
    if _current_keyword and "task_id" in _current_keyword:
        if "downloaded" in _current_keyword:
            return "downloading", (_current_keyword["downloaded"], _current_keyword["total"])
        else:
            return "fetching", None
    else:
        try:
            return "queued", _download_keyword.index(next(x for x in _download_keyword if x["task_id"] == task_id))
        except:
            return "not_present"

def get_training_status(task_id):
    """
    Return the status of the training task currently being fulfilled.
    TODO: Implement this method.
    """
    raise NotImplementedError()