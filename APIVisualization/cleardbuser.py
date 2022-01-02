print("---Clearing database---");

import pymongo
import pprint


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

githubuser = db.githubuser_single.delete_many({})