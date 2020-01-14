from flask_pymongo import pymongo
from .connection_string import MONGO_CONNECTION_STRING
from mongoengine import *
import ssl

#client = pymongo.MongoClient(MONGO_CONNECTION_STRING, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
# db = client.get_database('db_sensor')
# collection_sensor = db.collection_sensor

db = connect('db_sensor', host = MONGO_CONNECTION_STRING)
