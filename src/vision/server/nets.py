#
#   Networks database interface
#   Author: Yotam Salmon
#   Last Edited: 17/02/18
#

import database
import db_entities
from http_helper import msg

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
    ds = datasets.query(lambda c: c.get("owner_id") == user_id)
    return list(ds)

def get_classifiers(user_id):
    """
    Gets the classifier list for a specific user.
    Parametrs:
        user_id - (string) the id of the user
    Return value:
        the list of db_item representing the classifiers of the user.
    """
    classifiers = db.table("classifiers", db_entities.CLASSIFIER)
    cs = classifiers.query(lambda c: c.get("owner_id") == user_id)
    return list(cs)

def get_dataset(dataset_id):
    """
    Gets a dataset by id from the database
    Parameters:
        dataset_id - the db id of the dataset
    Return value:
        the db_item of the dataset.
    """
    datasets = db.table("datasets", db_entities.DATASET)
    ds = datasets.load_item(dataset_id)
    return ds or None

def delete_dataset(dataset_id, user_id):
    """
    Deletes a dataset from the database (but not its downloaded keywords)
    Parameters:
        dataset_id - the id of the dataset to remove
        user_id - the user that queried the action. Used for confirmation of deletion.
    Return value:
        None
    """
    datasets = db.table("datasets", db_entities.DATASET)
    
    ds = datasets.load_item(dataset_id)
    if ds is None:
        return 200, {}, msg("Dataset ID not found")

    if ds.get("owner_id") != user_id:
        return 403, {}, msg("Not the owner of the dataset")

    datasets.delete(ds)
    
    return 200, {}, msg("Dataset deleted")

def create_classifier(classifier_name, owner_id, dataset_id):
    """
    Creates a classifier in the database.
    """
    table = db.table("classifiers", db_entities.CLASSIFIER)

    # Trying to check for duplicated entries
    dups = table.query(lambda c: c.get("classifier_name") == classifier_name)
    if len(list(dups)) > 0:
        # Returning error message upon failure.
        return False, "Classifier name already exists in the database."

    # Checking that the owner id is an existing user.
    usr_tbl = db.table("users", db_entities.USER)
    usr = usr_tbl.load_item(owner_id)
    if usr is None:
        return False, "The requested owner of the classifier does not exist"

    # Checking that the dataset exists and is working
    ds_table = db.table("datasets", db_entities.DATASET)
    ds = ds_table.load_item(dataset_id)
    if ds is None or ds.get("working") == False:
        return False, "The dataset must exist and be ready to use"

    classifier = table.new() \
        .set("classifier_name", classifier_name) \
        .set("owner_id", owner_id) \
        .set("dataset_trained", dataset_id) \
        .set("date_trained", time.time()) \
        .set("trained", False)

    table.update(classifier)

    return True, classifier.item_id

def get_classifier(classifier_id):
    """
    Gets a classifier db object by its object id.
    """
    table = db.table("classifiers", db_entities.CLASSIFIER)
    return table.load_item(classifier_id) or None

def mark_trained(classifier_id, accuracy):
    """
    Marks a classifier as trained after the training process has been finished.
    """
    table = db.table("classifiers", db_entities.CLASSIFIER)
    classifier = table.load_item(classifier_id)

    if classifier is None:
        return False

    classifier.set("trained", True)
    classifier.set("accuracy", accuracy)
    table.update(classifier)
    
    return True