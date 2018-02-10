#
#   The trainer module to create classifiers based on datasets.
#   Author: Yotam Salmon
#   Last Edited: 10/02/2018
#

# Importing our task queues
import task_scheduler as ts

# Configuration variables
from constants import DEBUG, IMG_SIZE

# Utility imports 
import time

_working = True

def run():
    pass

def shutdown():
    """
    Shuts the trainer process down.
    """
    global _working
    _working = False

def _work():
    """
    The working thread. 
    """
    global _work
    while _working:
        # Getting the next task to perform
        el = ts.get_next_training_candidate()

        # Continue if there is no task awaiting.
        if el == None:
            time.sleep(1)
            continue

        # TODO: Do some job with the task.