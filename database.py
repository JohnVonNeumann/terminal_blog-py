import pymongo

class Database(object):
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)
    database = client['fullstack']
    collection = database['posts']
