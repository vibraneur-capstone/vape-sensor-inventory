import ssl

MONGO_CONNECTION_STRING = "mongodb://localhost:27017/inventory"
DATABASE_NAME = "inventory"
MONGO_CERT = ssl.CERT_NONE
SSL = MONGO_CONNECTION_STRING.find("localhost") == -1
