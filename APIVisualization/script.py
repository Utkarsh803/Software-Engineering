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
    token = input("Please enter the token or 'No' if using a username => ")
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


def get_data(top_repos,topic):
    print("Fetching repositories and their data for the topic: " + topic)
    for repo in top_repos:
        print("Fetching data for repository :  " + repo.name)
        for x in range(1,13):
            #setting times to specify to get commits for an interval
            s=datetime.datetime(2020,x,1)
            if x==2:
                u=datetime.datetime(2020,x,29)
            elif x!=2:
                u=datetime.datetime(2020,x,30)
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

            #print("Fetched data for repository :  " + json.dumps(dct['name']))

            conn = "mongodb://localhost:27017"
            client = pymongo.MongoClient(conn)

            db = client.classDB

            db.githubuser.insert_many([dct])

                

TOPICS=["machine-learning","data-science","Android-Studio","c++","java","javascript","python","react","Raspberry-pi","quantumn-computing"]
#list to keep track of all repos added
top_repo_full = []

for top in TOPICS:
    #search repos tagged with topics
    all_repo = g.search_repositories(f'topic:{top}')
    #get only first six repos from those repositories
    top_repo = []
    for i, repo in enumerate(all_repo):
        #check to not include duplicate repos again
        if repo not in top_repo_full:
            top_repo.append(repo)
            top_repo_full.append(repo)
        else:
            i=i-1
        if i == 5:
            break

    get_data(top_repo,top)

print("Fetching data through Github API. This might take some time.")
print("Data fetched successfully.")








