import os
from pymongo import MongoClient


def get_mongodb():
    client = MongoClient(
        host=f"mongodb+srv://gladkovnissan:{os.getenv('MONGODB_PASSWORD')}@cluster0.v0zgt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    )
    return client['max4']
   
db = get_mongodb()

if db is not None:
    try:
        db.command('ping')
        print("Connected to database:", db.name)
    except Exception as e:
        print("Could not connect to the database:", e)
else:
    print("Could not connect to the database: db is None")