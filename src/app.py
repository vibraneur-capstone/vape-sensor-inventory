from flask import Flask
import connexion
from flask_pymongo import pymongo
import repositories.db as DB

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yaml')

#test to insert data to the data base, meant to be removed later
@app.route("/test")
def test():
    DB.db.collection_sensor.insert_one({"name": "sensor_beta"})
    return "created a sensor"

if __name__ == '__main__':
    app.run(port=8822)