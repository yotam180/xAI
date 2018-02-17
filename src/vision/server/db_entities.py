#
#   Table structures for the database system
#   Author: Yotam Salmon    
#   Last Edited: 29/12/17
#

import database

USER = [
    "username",
    "password_hash",
    "first_name",
    "last_name",
    "phone_num",
    "country",
    "email"
]

SESSION = [
    "username",
    "expiery"
]

API_KEY = [
    "username",
    "creation_date"
]

DATASET = [
    "identifier",
    "owner_id",
    "subject",
    "description",
    "positive_keywords",
    "negative_keywords",
    "last_updated",
    "working"
]

CLASSIFIER = [
    "classifier_name",
    "owner_id",
    "dataset_trained",
    "date_trained",
    "trained"
]

REVIEW = [
    "classifier",
    "author",
    "rate",
    "comment",
    "date"
]

VOTE = [
    "classifier",
    "user",
    "sign"
]

db_instance = database.db("database")