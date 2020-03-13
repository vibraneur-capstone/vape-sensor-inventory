from .mongo_config import MONGO_CONNECTION_STRING, DATABASE_NAME, MONGO_CERT, SSL
from mongoengine import connect

def connect_db():
    connect(DATABASE_NAME, host=MONGO_CONNECTION_STRING, ssl=SSL, ssl_cert_reqs=MONGO_CERT)



