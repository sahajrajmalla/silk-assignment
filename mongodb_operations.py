from pymongo import MongoClient, errors
from config import MONGO_URI, DB_NAME

# MongoDB Connection
def get_mongo_client():
    return MongoClient(MONGO_URI)

def get_mongo_collection(client, collection_name):
    db = client[DB_NAME]
    return db[collection_name]

def create_unique_index(collection, field):
    try:
        collection.create_index(field, unique=True)
        print(f"Created unique index on '{field}' in collection '{collection.name}'")
    except Exception as e:
        print(f"Error creating index: {e}")
