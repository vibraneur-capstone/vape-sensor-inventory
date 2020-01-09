from flask import Flask
import connexion
from flask_pymongo import pymongo
from .connection_string import MONGO_CONNECTION_STRING
from app import app

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client.get_database('db_sensor')
collection_sensor = db.collection_sensor