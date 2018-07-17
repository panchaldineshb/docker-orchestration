from pymongo import MongoClient
import logging as log
import json

log.basicConfig(format="[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s", level=log.DEBUG)
log.info("Verbose output.")
log.info("This should be verbose.")
log.warning("This is a warning.")
log.error("This is an error.")

client = MongoClient(['myhostname:27017'])
log.info(client)
log.info("Connection Successful")
log.info(client.database_names())
client.close()
