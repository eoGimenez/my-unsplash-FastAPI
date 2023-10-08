from pymongo.mongo_client import MongoClient

URL_DB = "mongodb://127.0.0.1:27017/"

client = MongoClient(URL_DB)
db = client["my-unsplash-master"]
collection = db.images

def get_db():
    try:
        yield client.command()