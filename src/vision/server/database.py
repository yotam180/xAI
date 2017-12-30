#
#   Database module
#   Author: Yotam Salmon
#   Last Edited: 29/12/17
#

import json
import os
from random import randint

class db(object):
    """
    Represents a database object.
    """
    def __init__(self, basepath):
        """
        Initialises a new database object. Receives the database's base path.
        """
        self.basepath = basepath
    
    def table(self, name, template):
        """
        Loads a table from the database
        """
        return db_table(self, name, template)

class db_table(object):
    """
    Represents a database table
    """
    def __init__(self, db, name, template):
        self.db = db
        self.name = name
        self.template = template
        if not os.path.exists(self.path()):
            os.makedirs(self.path())
    
    def path(self):
        return os.path.join(self.db.basepath, self.name)

    def new(self):
        rndstr = "1234567890aBcDeFgHiJkLmNoPqRsTuVwXyZ"
        _id = ""
        while _id == "" or _id + ".json" in os.listdir(self.path()):
            _id = "".join([rndstr[randint(0, len(rndstr ) - 1)] for x in range(20)])
        i = db_item(self, _id, {})
        return i

    def update(self, item):
        with open(os.path.join(self.path(), item.item_id + ".json"), "w") as f:
            f.write(json.dumps(item.data))

    def delete(self, item):
        if os.path.exists(os.path.join(self.path(), item.item_id + ".json")):
            os.unlink(os.path.join(self.path(), item.item_id + ".json"))
    
    def load_item(self, item_id):
        if not os.path.exists(os.path.join(self.path(), item_id)):
            return None
        with open(os.path.join(self.path(), item_id), "r") as f:
            data = json.loads(f.read())
        item = self.new()
        item.item_id = item_id.replace(".json", "")
        item.data = data
        return item

    def query(self, filter = None):
        ids = [x for x in os.listdir(self.path()) if x.endswith(".json")]
        for i in ids:
            item = self.load_item(i)
            if not filter or filter(item):
                yield item

class db_item(object):
    """
    Represents a database item.
    """
    def __init__(self, table, id, data):
        self.table = table
        self.data = data or {}
        self.item_id = id
    
    def get(self, col):
        if col in self.table.template:
            if col in self.data.keys():
                return self.data[col]
            else:
                return None
        else:
            raise KeyError()
    
    def set(self, col, val):
        if col in self.table.template:
            self.data[col] = val
        else:
            raise KeyError()
        return self

# def query(table_name, filter=None):
#     path = os.path.join("database", table_name)
#     if not os.path.exists(path):
#         os.makedirs(path)
#     iters = [x for x in os.listdir(path) if x.endswith(".json")]
#     for item in iters:
#         with open(x, "r") as f:
        