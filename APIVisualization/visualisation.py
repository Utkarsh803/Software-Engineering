import pandas as pd
from pandas.core.frame import DataFrame
import plotly
import plotly.express as px
import plotly.io as pio

#extracting data from csv to pandas dataframe
col_names = ["Topic","Name","Month","Full_Name","language","Forks","Stars","PRs_Count","Contributors_Count","Watchers_Count","Commits","Issues","Topics"]
df = pd.read_csv('repoData.csv', names=col_names)

#drop first row with field names
df.drop(0,axis=0,inplace=True)

#convert fields to integer
cols = ['Stars','Month','Forks','Issues','PRs_Count','Commits','Contributors_Count','Watchers_Count']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)


# create a dataframe with average values of the columns across all Names
df_name_Stars = (df.groupby('Name').mean().reset_index()).nlargest(5,['Stars'])


#extract the reponames with most Stars
top_names_Stars=[]
for name in df_name_Stars['Name']:
    top_names_Stars.append(name)
  
#------------------------------------------------------figure1-------------------------------------------
#filter original data with top repo names
f_Stars=df.query("Name==@top_names_Stars")

#remove duplicate data
f_Stars = f_Stars.drop(f_Stars[(f_Stars['Month'] >1)].index)

#plot a barchart to show repos with most Stars
plot = px.bar(
    data_frame=f_Stars,
    x="Name",
    y="Stars",
    color="Name",           
    opacity=0.9,               
    orientation="v",            
    barmode='relative',           
    labels={"Name":"Name",
    "Name":"Name"},           
    title='Top 5 Starred Repositories ',              
    template='plotly_dark',            
)

plot.show()
#----------------------------------------figure 2----------------------------------------
#shows the commits freuency on repos by month.
#Get the repositories with the top commits in 2020
df_name_commits = (df.groupby('Name').mean().reset_index()).nlargest(5,['Commits'])
top_names_commit=[]
for name in df_name_commits['Name']:
    top_names_commit.append(name)
#plot the repos with most commits on a line chart
f_commit=df.query("Name==@top_names_commit")
#set names for months
calendar = {1 : 'January',2 : 'February',3 : 'March',4 : 'April',5 : 'May',6 : 'June',7 : 'July',8 : 'August',9 : 'September',10 : 'October',11 : 'November',12 : 'December'}
f_commit.Month = [calendar[item] for item in f_commit.Month]
#plot the commits on a line chart
figTwo = px.line(f_commit, x="Month", y="Commits", color='Name',title="Commit Trend of Repositories with top commits 2020")
figTwo.show()


#----------------------------------figure 3----------------------------------------------
#plot heatmap of the contributions and pull request,issues,commits.
df_name = (df[['Name','PRs_Count','Contributors_Count','Issues','Commits','Stars']].groupby('Name').mean().reset_index())

df_name = df_name.loc[(df_name["Commits"] > 0) & (df_name["Stars"] > 0) & (df_name["Issues"] > 0) & (df_name["PRs_Count"] > 0) & (df_name["Contributors_Count"] > 0)]

#getting least popular repos
df_smallest = df_name.nsmallest(5,['Stars'])
#getting most popular repos
df_largest = df_name.nlargest(5,['Stars'])
#dropping stars column we have alredy arranged data we wanted
df_smallest=df_smallest.drop('Stars', axis=1)
#find correlation between factors for least popular repos
corrMatrixSmall=df_smallest.corr()
fig = px.imshow(corrMatrixSmall, title="Relationship of Contributors Count with other factors of least popular repos from the data.")
fig.show()

#find correlation between factors for most popular repos
df_largest=df_largest.drop('Stars', axis=1)
corrMatrixLarge=df_largest.corr()
fig = px.imshow(corrMatrixLarge, title="Relationship of Contributors Count with other factors of most popular repos from the data.")
fig.show()