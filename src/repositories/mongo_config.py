import ssl

MONGO_CONNECTION_STRING = "DB-CONNECTION"
DATABASE_NAME = "inventory"
MONGO_CERT = ssl.CERT_NONE
HEADER = {"Access-Control-Allow-Origin": "*"}