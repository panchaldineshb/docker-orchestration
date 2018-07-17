from pymongo import MongoClient
import logging as log
import json

log.basicConfig(format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", level=log.DEBUG)
log.info("Verbose output.")
log.info("This should be verbose.")
log.warning("This is a warning.")
log.error("This is an error.")

uri = 'mongodb://myhostname:27017/local'
client = MongoClient(uri)
log.info(client)
log.info("Connection Successful")
db = client.get_default_database()
log.info(db)
db = client.get_database()
log.info(db)
client.close()
