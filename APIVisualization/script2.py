print("Lets fetch the data from db");

import pymongo
import pprint


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

githubuser = db.githubuser.find()

for user in githubuser:
    pprint.pprint(user)
    print()
