#
#   Networks database interface
#   Author: Yotam Salmon
#   Last Edited: 31/12/17
#

import database
import db_entities

db = db_entities.db_instance

def create_dataset(dataset_name: str, positives: list, negatives: list, owner: database.db_item, subject: str, description: str) -> database.db_item:
    pass