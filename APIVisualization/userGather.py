#import Github from the pyGithub library
from github import Github
import json
import pymongo
import datetime
import os
import pandas as pd 
import datetime

# using an access token--create own token to use
g = Github("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")

#getting basic user data
usr = g.get_user()

#print("Getting data for repo:" + repo_name);

#get repo by name
#repo = g.get_repo(repo_name)
            
def get_user_data():
            repositories=usr.get_repos()
            for repo in repositories:
                dct ={'User_Name':usr.name,
                      'name': repo.name,
                      'language': repo.language,
                      'Forks':repo.forks_count,
                      'Stars':repo.stargazers_count,
                      'Commits': repo.get_commits().totalCount,
                      'Commit_info': [i._rawData for i in repo.get_commits()]
                      }

                    #store the dictionary in database
                for k, v in dict(dct).items():
                            if v is None:
                                del dct[k]

               # print("Cleaned Dictionary:  " + json.dumps(dct))

                conn = "mongodb://localhost:27017"
                client = pymongo.MongoClient(conn)

                db = client.classDB

                db.githubuser_single.insert_many([dct])
    

get_user_data()



