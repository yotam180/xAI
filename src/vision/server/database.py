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
    def __init__(self, basepath: str):
        """
        Initialises a new database object. Receives the database's base path.
        """
        self.basepath = basepath
    
    def table(self, name, template):
        """
        Loads a table from the database
        """
        return db_table(self, name, template)

class db_item(object):
    """
    Represents a database item.
    """
    def __init__(self, table, id, data):
        """
        Initialising a new item object.
        """
        self.table = table
        self.data = data or {}
        self.item_id = id
    
    def get(self, col: str):
        """
        Gets a column from the record row.
        """
        if col in self.table.template:
            if col in self.data.keys():
                return self.data[col]
            else:
                return None
        else:
            raise KeyError()
    
    def set(self, col: str, val):
        """
        Sets a column of the record row.
        """
        if col in self.table.template:
            self.data[col] = val
        else:
            raise KeyError()
        return self

class db_table(object):
    """
    Represents a database table
    """
    def __init__(self, db: db, name: str, template: list):
        """
        Initialises a new instance of a db_table. Should not be called directly, use db.table() insted.
        """

        # Updating all self properties
        self.db = db
        self.name = name
        self.template = template

        # If the requested table was never accessed on disk, we create it.
        if not os.path.exists(self.path()):
            os.makedirs(self.path())
    
    def path(self) -> str:
        """
        Returns the path of the directory on disk of the table.
        """
        return os.path.join(self.db.basepath, self.name)

    def new(self) -> db_item:
        """
        Creates a new record in the table. Does not store it yet on the disk. Best to write it
        immediately after initialisation to avoid duplicated IDs. 
        """

        # Randomising an ID
        rndstr = "1234567890aBcDeFgHiJkLmNoPqRsTuVwXyZ"
        _id = ""

        # Guaranteeing that the ID is not duplicated (what are the odds, anyways?) 
        while _id == "" or _id + ".json" in os.listdir(self.path()):
            _id = "".join([rndstr[randint(0, len(rndstr ) - 1)] for x in range(20)])

        # Creating a new (empty) database item with the generated ID, and returning it.
        i = db_item(self, _id, {})
        return i

    def update(self, item: db_item) -> None:
        """
        Updating an item on disk from an in-memory item.
        If the item does not exist on disk, creating it.
        """
        with open(os.path.join(self.path(), item.item_id + ".json"), "w") as f:
            f.write(json.dumps(item.data))

    def delete(self, item: db_item) -> None:
        """
        Deleting an item in memory from the disk. Note: does not remove the item object
        from the memory.
        """
        if os.path.exists(os.path.join(self.path(), item.item_id + ".json")):
            os.unlink(os.path.join(self.path(), item.item_id + ".json"))
    
    def load_item(self, item_id: str) -> db_item:
        """
        Loading an item from memory by its id.
        """
        
        # Checking if the item exists on disk, and if not - returning None.
        if not os.path.exists(os.path.join(self.path(), item_id + ".json")):
            return None

        # Reading the item from disk
        with open(os.path.join(self.path(), item_id + ".json"), "r") as f:
            data = json.loads(f.read())

        # Constructing a new item and updatnig the data and id
        item = self.new()
        item.item_id = item_id
        item.data = data
        
        # Returning the constructed item
        return item

    def query(self, filter = None):
        """
        Creates a generator to iterate all items that satisfy a predicate. (or all records from the
        table if the filter is not specified)
        """

        # Listing all records of a specific table
        ids = [x for x in os.listdir(self.path()) if x.endswith(".json")]

        # Iterating through all them
        for i in ids:
            # Loading the item
            item = self.load_item(i[:-5])

            # Passing through the filter
            if not filter or filter(item):
                # Yielding the next result
                yield item
