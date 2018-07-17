from pymongo import MongoClient
import json

log.basicConfig(format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", level=log.DEBUG)
log.info("Verbose output.")
log.info("This should be verbose.")
log.warning("This is a warning.")
log.error("This is an error.")

client = MongoClient("mongodb://127.0.0.1:27017")
log.info("Connection Successful")

d = dict((db, [collection for collection in client[db].collection_names()])
         for db in client.database_names())
log.info(json.dumps(d))

client.close()
