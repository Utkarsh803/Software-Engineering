print("Saving data to csv files...");

import pymongo
import pprint
from datetime import date
from datetime import datetime
import numpy as np

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB

userName=""

dct = db.githubuser_single.find()

"""
for user in dct:
    pprint.pprint('User Name : '+ user['User_Name'])
    pprint.pprint('Name : '+ user['name'])
    if user.get('language') is not None:
     pprint.pprint('Language : '+ user['language'])
    pprint.pprint('Forks : '+str(user['Forks']))
    pprint.pprint('Stars : '+ str(user['Stars']))
    pprint.pprint('Commits : '+ str(user['Commits']))
    print()
"""

print("Saving user info in userInfo.csv")
with open('userInfo.csv', 'w') as f:
    f.write('User_Name,Name,Language,Forks,Stars,Commits\n')
    dct = db.githubuser_single.find()
    for user in dct:
        if user.get('language') is not None and user.get('User_Name') is not None and user.get('name') is not None:
            f.write(user['User_Name']+','+user['name']+','+user['language']+','+str(user['Forks'])+','+str(user['Stars'])+','+str(user['Commits'])+'\n')
            userName=user['User_Name']


print("Saving user commit history info in commit_history.csv")
with open('commit_history.csv', 'w') as f:
    f.write('Datetime,Commit,Week,Day\n')
    dct = db.githubuser_single.find()
    for user in dct:
        if user.get('language') is not None:
            lenn=len((user['Commit_info']))
            pprint.pprint((user['name']))
            print()
            name=user['name']
            for l in (user['Commit_info']):
                if (l['commit']['author']['name']==userName):
                    pprint.pprint((l['commit']['author']['date']))
                    print()
                    dateT=(l['commit']['author']['date'])
                    dateT= dateT.split("T")
                    fdate=datetime.fromisoformat(dateT[0])
                    f.write(dateT[0]+','+"1"+','+str(fdate.isocalendar()[1]) +',' + str(fdate.isocalendar()[2])+'\n')

print("Data saved successfully. Now visualising....")

