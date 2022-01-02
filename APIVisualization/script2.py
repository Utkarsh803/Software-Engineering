print("Feching data from database and saving into csv file.");

import pymongo
import pprint


conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.classDB
#save data to a csv
with open('repoData.csv', 'w') as f:
    f.write('Topic,Name,Month,Full_Name,language,Forks,Stars,PRs_Count,Contributors_Count,Watchers_Count,Commits,Issues,Topics\n')
    dct = db.githubuser.find()
    for user in dct:     
        if user.get('language') is not None:
            f.write(user['Topic']+','+user['name']+','+str(user['Month'])+','+ user['Full_Name']+ ','+ user['language']+','+str(user['Forks'])+','+ str(user['Stars'])+','+  str(user['PRs_Count'])+','+  str(user['Contributors Count'])+ ','+ str(user['Watchers Count'])+ ','+ str(user['Commits'])+ ','+ str(user['Issues'])+','+ str(user['Topics'])+'\n')

print("Data saved into csv file. Now visualising....");