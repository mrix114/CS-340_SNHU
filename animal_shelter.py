from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections        
        self.client = MongoClient('localhost:54011',
                                  username=username,
                                  password=password,
                                  authSource='AAC')
        self.database = self.client['AAC']

    #Inserts a single entry into the database from the user-supplied data.
    #Returns True if create operation was successful, otherwise returns False.
    def create(self, data):
        if data is not None:            
            result = self.database.animals.insert_one(data) # data should be dictionary     
            return result.acknowledged
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
       
    #Queries database for data and returns a Cursor containing the first matching entry.
    def readOne(self, data):
        if data is not None:
            return self.database.animals.find_one(data)
        else:
            raise Exception("nothing to read because data parameter is empty")
            

    #Queries database for data and returns a Cursor containing all matching entries.
    def readAll(self, data):
        if data is not None:
            return self.database.animals.find(data,{"_id":False})
        else:
            raise Exception("nothing to read because data parameter is empty")
    
    #Queries database for data and updates all matching entries with the supplied key/value pair.
    #Returns JSON-formatted result data via the raw_result field.
    def update(self, data, update_key, update_value):
        if data is not None:
            result = self.database.animals.update_many(data, {'$set':{update_key:update_value}})   
            return result.raw_result
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            
    #Queries database for data and deletes all matching entries.
    #Returns JSON-formatted result data via the raw_result field.
    def delete(self, data):
        if data is not None:
            result = self.database.animals.delete_many(data)
            return result.raw_result
        else:
            raise Exception("nothing to read because data parameter is empty")

            