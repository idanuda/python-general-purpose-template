import pymongo
import certifi
from decouple import config

client = pymongo.MongoClient(config("ATLAS_QA_CONN_STRING"), serverSelectionTimeoutMS=5000, tlsCAFile=certifi.where())


def get_server_info(collection_name, doc_id):
    doc = {}
    try:
        doc = client.get_database('prod').get_collection(collection_name).find_one({'_id': doc_id})
    except Exception:
        print("Unable to connect to the server.")
    return doc
