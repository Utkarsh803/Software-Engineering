import pandas as pd
from pandas.core.frame import DataFrame
import plotly
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots

#extracting data from csv to pandas dataframe
col_names = ["Topic","Name","Month","Full_Name","language","Forks","Stars","PRs_Count","Contributors_Count","Watchers_Count","Commits","Issues","Topics"]
df = pd.read_csv('moreData.csv', names=col_names)

#drop first rowwith field names
df.drop(0,axis=0,inplace=True)

#convert fields to integer
cols = ['Stars','Month','Forks','Issues','PRs_Count','Commits','Contributors_Count','Watchers_Count']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce', axis=1)


# create a dataframe with average values of the columns across all Names
df_name_Stars = (df.groupby('Name').mean().reset_index()).nlargest(5,['Stars'])
#print(df_name)

#extract the reponames with most Stars
top_names_Stars=[]
for name in df_name_Stars['Name']:
    top_names_Stars.append(name)
    #print(top_names)


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
    #width=700,                
    #height=700,                
    template='plotly_dark',            
)

plot.show()
