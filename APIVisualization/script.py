#import Github from the pyGithub library
from github import Github
import json
import pymongo
import datetime


# using an access token--create own token to use
g = Github("")

#getting basic user data
usr = g.get_user()


#take user input--repo name
repo_name = input("Enter repo name: ")

print("Getting data for repo:" + repo_name);

#get repo by name
repo = g.get_repo(repo_name)

#get repo pulls
PRs=repo.get_pulls(state='all')

#storing repo data into dictionary
dct ={'id': repo.id,
           'name': repo.name,
           'Full Name' :repo.full_name,
           'language': repo.language,
           'Date created': (repo.created_at).strftime('%m/%d/%Y'),
           'Date of last push': (repo.pushed_at).strftime('%m/%d/%Y'),
           'Forks':repo.forks_count,
           'Stars':repo.stargazers_count,
           'Topics': repo.get_topics(),
           'Watchers': repo.subscribers_count,
           'PRs_Count': PRs.totalCount,
           'Labels': [i._rawData for i in repo.get_labels()],
           'Contributors': [i._rawData for i in repo.get_contributors()],
            'Contributors Count': repo.get_contributors().totalCount,
            #"Subscribers": [i._rawData for i in repo.get_subscribers()],
            'Subscribers Count': repo.get_subscribers().totalCount,
            #"Watchers": [i._rawData for i in repo.get_watchers()],
            'Watchers Count': repo.get_watchers().totalCount  
          }

#store the dictionary in database
for k, v in dict(dct).items():
        if v is None:
            del dct[k]

print("Cleaned Dictionary:  " + json.dumps(dct))

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

db.githubuser.insert_many([dct])






