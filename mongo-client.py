from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27017")
print("Connection Successful")
client.close()


import pymongo
import json

if __name__ == '__main__':
    client = pymongo.MongoClient("localhost", 27017, maxPoolSize=50)
    d = dict((db, [collection for collection in client[db].collection_names()])
             for db in client.database_names())
    print json.dumps(d)
    
