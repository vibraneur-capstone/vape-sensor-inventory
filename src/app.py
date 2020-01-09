from flask import Flask
import connexion
from flask_pymongo import pymongo
import os

MONGO_URI = os.environ.get('MONGO_CONNECTION_STRING')
app = connexion.App(__name__, specification_dir='./')
client = pymongo.MongoClient("mongodb+srv://db-vape-sensor-inventory:theMostSecurePassword?!@cluster-vape-sensor-inventory-fcfqt.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('db_sensor')
collection_sensor = db.collection_sensor


@app.route("/")
def index():
    db.collection_sensor.insert_one({"name": "sensor_beta"})
    return "created a sensor"

if __name__ == '__main__':
    app.run(port=8822)