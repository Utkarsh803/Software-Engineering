#import Github from the pyGithub library
from github import Github
import json
import pymongo


# using an access token--create own token to use
g = Github("")

#getting basic user data
usr = g.get_user()


dct = {'user': usr.login,
       'fullname': usr.name,
       'location': usr.location,
       'company': usr.company
}
print("Dictionary:  " + json.dumps(dct))


#store the dictionary in database
for k, v in dict(dct).items():
    if v is None:
        del dct[k]

print("Cleaned Dictionary:  " + json.dumps(dct))

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

db.githubuser.insert_many([dct])



