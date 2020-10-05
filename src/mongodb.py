"""mongodb.py
Contains the configuration for the mongo database and makes the connection using the pymongo python library.
Takes the configuration to connect to database from the environment (MONGO_URI) but has a default.
"""

from os import environ
from pymongo import MongoClient


MONGO_URI = environ.get("MONGO_URI", default="mongodb://localhost:27017")

client = MongoClient(MONGO_URI)
mongo_db = client['tasks']
