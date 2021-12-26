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

def get_data(top_repos,topic):
    for repo in top_repos:
        for x in range(1,13):
            s=datetime.datetime(2020,x,1)
            if x==2:
                u=datetime.datetime(2020,x,29)
            elif x!=2:
                u=datetime.datetime(2020,x,29)
            PRs=repo.get_pulls(state='all')
            all_issues = repo.get_issues(state='open',sort='created',direction='asc')
            dct ={'Topic':topic,
                    'Month':x,
                        'name': repo.name,
                        'Full_Name' :repo.full_name,
                        'language': repo.language,
                        'Forks':repo.forks_count,
                        'Stars':repo.stargazers_count,
                        'Topics': repo.get_topics(),
                        'PRs_Count': PRs.totalCount,
                        'Contributors Count': repo.get_contributors().totalCount,
                        'Watchers Count': repo.get_watchers().totalCount,
                        'Commits': repo.get_commits(since=s,until=u).totalCount,
                        'Issues' : all_issues.totalCount
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

                

TOPICS=["machine-learning","data-science","Android-Studio","c++","java","javascript","python","react","Raspberry-pi","quantumn-computing"]

for top in TOPICS:
    all_repo = g.search_repositories(f'topic:{top}')
    #print(all_repo.totalCount)

    top_repo = []
    for i, repo in enumerate(all_repo):
        top_repo.append(repo)
        if i == 20:
            break

    get_data(top_repo,top)








