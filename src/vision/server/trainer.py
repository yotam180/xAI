#
#   The trainer module to create classifiers based on datasets.
#   Author: Yotam Salmon
#   Last Edited: 17/02/2018
#

# Importing our task queues
import task_scheduler as ts

# Configuration variables
from constants import DEBUG, IMG_SIZE

# Utility imports 
import time

# Other internal modules
import nLib as nl
import nets

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

        # Defining our evaluation model
        print("Loading dataset " + el["dataset_id"])

        ds = nets.get_dataset(dataset_id)
        if ds == None:
            # Cheking if the dataset exists, otherwise throwing an error
            # and rage quitting the process.
            el["err"] = "Dataset ID not found"
            ts.finished_download(el)
            continue

        dataset = nl.load_dataset(
            ds.get("positive_keywords"),
            ds.get("negative_keywords")
        )

        net = nl.train_classifier(dataset)

        # TODO: continue this method, saving and updating 
        # the database about the trained classifier.