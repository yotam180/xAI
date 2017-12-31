#
#   Networks database interface
#   Author: Yotam Salmon
#   Last Edited: 31/12/17
#

import database
import db_entities

import time

db = db_entities.db_instance

def create_dataset(dataset_name: str, positives: list, negatives: list, owner: database.db_item, subject: str, description: str) -> database.db_item:
    datasets = db.table("datasets", db_entities.DATASET)
    
    # Checking for duplicate IDs in existing datasets.
    duplicates = len(list(datasets.query(
        lambda c: c.get("identifier") == dataset_name
    )))
    if duplicates > 0:
        return False, "Dataset ID already exists"

    dataset = datasets.new() \
        .set("identifier", dataset_name) \
        .set("username", owner.get("username")) \
        .set("subject", subject) \
        .set("description", description) \
        .set("positive_keywords", positives) \
        .set("negative_keywords", negatives) \
        .set("last_updated", time.time())

    datasets.update(dataset)

    return True, None