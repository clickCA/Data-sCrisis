from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError


def store_in_mongo(
    myclient,
    data_collections,
    database="scopus_db",
    collection_name="scopus_collection",
):
    db = myclient[database]
    collection = db[collection_name]
    for data in data_collections:
        try:
            collection.insert_one(data)
        except DuplicateKeyError:
            # If duplicate _id is found, replace the existing document with the new one
            collection.replace_one({"_id": data["_id"]}, data)
