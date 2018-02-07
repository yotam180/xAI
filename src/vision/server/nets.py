#
#   Networks database interface
#   Author: Yotam Salmon
#   Last Edited: 31/12/17
#

import database
import db_entities

import time

db = db_entities.db_instance

def create_dataset(dataset_name: str, positives: list, negatives: list, owner_id: str, subject: str, description: str) -> database.db_item:
    """
    Registers a new dataset into the database.
    Parameters:
        dataset_name - the identifier of the dataset
        positives - the positive keywords to trigger the classifier
        negatives - the negative keywords to restrict the classifier
        owner_username - the username of the owner of the dataset
        subject - the textual description of the dataset subject
        description - a description about what the subject is

    Return Value:
        the id of the database record just created. 
    """
    datasets = db.table("datasets", db_entities.DATASET)
    
    # Checking for duplicate IDs in existing datasets.
    duplicates = len(list(datasets.query(
        lambda c: c.get("identifier") == dataset_name
    )))
    if duplicates > 0:
        return False, "Dataset ID already exists"

    dataset = datasets.new() \
        .set("identifier", dataset_name) \
        .set("owner_id", owner_id) \
        .set("subject", subject) \
        .set("description", description) \
        .set("positive_keywords", positives) \
        .set("negative_keywords", negatives) \
        .set("last_updated", time.time()) \
        .set("working", False)

    datasets.update(dataset)

    return True, dataset.item_id

def set_working(dataset_id):
    """
    After downloading all the keywords, we have to update the database
    entity to make sure our dataset is marked as "working"
    """

    datasets = db.table("datasets", db_entities.DATASET)

    ds = datasets.load_item(dataset_id)
    if ds is None:
        return False

    ds.set("working", True)
    datasets.update(ds)

    return True

def get_datasets(user_id):
    """
    Gets the dataset list for a specific user.
    Parametrs:
        user_id - (string) the id of the user
    Return value:
        the list of db_item representing the datasets of the user.
    """
    datasets = db.table("datasets", db_entities.DATASET)
    ds = datasets.query(lambda c: c.get("user_id") == user_id)
    return list(ds)