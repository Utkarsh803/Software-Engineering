import pprint
import pandas as pd 
from datetime import date
from datetime import datetime
import numpy as np
import plotly.express as px


name=" "

df_user=pd.read_csv('userInfo.csv')
repos= df_user.shape[0]
name=df_user['User_Name'][0] 
#get total number of forks, stars, commits on repos
forks = df_user['Forks'].sum()     
Stars = df_user['Stars'].sum()     
commits = df_user['Commits'].sum()     

#calculating language percentage based on how may repos use them
df_lang=df_user['Language'].value_counts(normalize=True) * 100

#------------------------------------------------------pie chart---------------------
#plotting pie chart for them
fig = px.pie(df_lang, values='Language', names=df_lang.index, title='Most used languages')
fig.show()

#---------------------------------------------------bar chart---------------------------------

#plotting the repos according to their stars in a bar chart
figTwo = px.bar(df_user, x='Name', y='Stars', title='Most starred repositories')
figTwo.show()


#------------------------------------------------------Commit heapmap-------------------------------

#visualization of user commit frequency
df=pd.read_csv('commit_history.csv')
#count total commit which is equal to number of rows
total_commits=count_row = df.shape[0]
#adding missing dates for the year in our dataframe
df['Datetime'] = pd.to_datetime(df['Datetime'])
idx = pd.date_range('2021-01-01','2021-12-31')
#arranging dates based on their commit numbers
df = pd.pivot_table(df, index=['Datetime'],values=['Commit'],aggfunc='sum')
df.index = pd.DatetimeIndex(df.index)
#fill 0 commits for missing dates
df = df.reindex(pd.date_range("2021-01-01", "2021-12-31"), fill_value=0)

week=[]
day=[]

dates=(df.index).to_pydatetime()
#adding the week and day number to our dataframe 
for dat in dates:
    day.append(dat.isocalendar()[2])
    week.append(dat.isocalendar()[1])

df['Day'] = day
df['Week'] = week
#creating a 3D matrix for our heatmap 
commit_matrix = df.pivot("Day", "Week", "Commit")
#labeling numeral days to names
y_axis_labels = ['Mon','Tue','Wed','Thur','Fri','Sat','Sun']
#plotting basing info as title
titl=("Name :" + name +'\t'+"Repos: "+str(repos)+'<br>'+"Total Commits in 2021: "+ str(total_commits)+'\t'+"Total Stars on Repos: "+str(Stars)+'<br>'+"User Commit Trend in 2021 :"+"\n").expandtabs(30)
#plot the heatmap
fig = px.imshow(commit_matrix, y=['Mon', 'Tue', 'Wed', 'Thur', 'Fri','Sat','Sun'], title=(titl))
fig.show()


