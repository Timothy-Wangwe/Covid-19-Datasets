#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import 3rd party libraries
import urllib.request
import json
import pandas as pd
from datetime import datetime


# In[2]:


# Fetch data from api


# In[3]:


url = 'https://api.covid19api.com/summary'


# In[4]:


JsonObj = urllib.request.urlopen(url)
JsonObj


# In[5]:


Obj = json.load(JsonObj)


# In[6]:


# Iterate though, filter and save data


# In[7]:


Countries = []
Cases = []
nCases = []
Deaths = []
nDeaths = []
Recoveries = []
nRecoveries = []


# In[8]:


for item in Obj['Countries']:
    Countries.append(item['Country'])
    Cases.append(item['TotalConfirmed'])
    nCases.append(item['NewConfirmed'])
    Deaths.append(item['TotalDeaths'])
    nDeaths.append(item['NewDeaths'])
    Recoveries.append(item['TotalRecovered'])
    nRecoveries.append(item['NewRecovered'])


# In[9]:


# Create a pandas dataframe
DataLib = {
    "Countries" : Countries,
    "Total Cases" : Cases,
    "New Cases" : nCases,
    "Total Deaths" : Deaths,
    "New Deaths" : nDeaths,
    "Total Recoveries" : Recoveries,
    "New Recoveries" : nRecoveries
}

cols = DataLib.keys()

data = pd.DataFrame(DataLib, columns = cols)
data.head()


# In[12]:


# Save to csv file as current date
name = datetime.now().strftime("%d-%b-%Y")
data.to_csv(f'Data-Sets/{name}.csv')


# In[ ]:




