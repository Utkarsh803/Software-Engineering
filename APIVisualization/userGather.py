#import Github from the pyGithub library
from github import Github
import json
import pymongo
import datetime
import os
import pandas as pd 
import datetime

# using an access token--create own token to use

try:
    token = input("Please enter the token or no if using a username => ")
    g = Github(token)
    usr = g.get_user()
    test_token_repos=usr.get_repos()
    for repo in test_token_repos:
        break
    print("Token worked.Getting data..")
except:
    print("Token is invalid.You have limited access.")
    username = input("Enter your Github Username =>")
    g = Github()
    usr = g.get_user(username)
    

#specify the time to get commits for an interval
sincetime=datetime.datetime(2021,1,1)
untiltime=datetime.datetime(2021,12,31)
            
def get_user_data():
            print("Fetching data for the user...")
            #get user repos
            repositories=usr.get_repos()
            for repo in repositories:
                dct ={'User_Name':usr.name,
                      'name': repo.name,
                      'language': repo.language,
                      'Forks':repo.forks_count,
                      'Stars':repo.stargazers_count,
                      'Commits': repo.get_commits().totalCount,
                      'Commit_info': [i._rawData for i in repo.get_commits(since=sincetime, until=untiltime)]
                      }

                #store the dictionary in database
                for k, v in dict(dct).items():
                            if v is None:
                                del dct[k]

                print("Fetched data for repository :  " + json.dumps(dct['name']))

                conn = "mongodb://localhost:27017"
                client = pymongo.MongoClient(conn)

                db = client.classDB

                db.githubuser_single.insert_many([dct])
    

get_user_data()

print("Data fetched successfully.")



