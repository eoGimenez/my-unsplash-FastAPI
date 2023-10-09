from pymongo.mongo_client import MongoClient

URL_DB = "mongodb://127.0.0.1:27017/"

client = MongoClient(URL_DB)
db = client["my-unsplash-master"]
collection = db.images

def get_db():
    client.admin.command('ping')
    try:
        yield collection
    except:
        print(f'Hubo algun error intentando acceder a la coleción: {collection.name}')
