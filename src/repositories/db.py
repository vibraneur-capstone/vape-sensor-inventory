from flask_pymongo import pymongo
from .connection_string import MONGO_CONNECTION_STRING
from mongoengine import *
import ssl

db = connect('db_sensor', host = MONGO_CONNECTION_STRING, ssl=True, ssl_cert_reqs=ssl.CERT_NONE)
