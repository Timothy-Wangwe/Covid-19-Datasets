#______________
#Timothy Wangwe
#==============

# Add module to system path
import sys
sys.path.append("../")

# Import 3rd party libraries
import urllib.request
import json
import pandas as pd
from datetime import datetime
import time
from AutoGit import auto

def fetch():
    # Fetch data from api
    url = 'https://api.covid19api.com/summary'
    JsonObj = urllib.request.urlopen(url)
    Obj = json.load(JsonObj)

    # Iterate though, filter and save data

    Countries = []
    Cases = []
    nCases = []
    Deaths = []
    nDeaths = []
    Recoveries = []
    nRecoveries = []

    for item in Obj['Countries']:
        Countries.append(item['Country'])
        Cases.append(item['TotalConfirmed'])
        nCases.append(item['NewConfirmed'])
        Deaths.append(item['TotalDeaths'])
        nDeaths.append(item['NewDeaths'])
        Recoveries.append(item['TotalRecovered'])
        nRecoveries.append(item['NewRecovered'])

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

    # Save to csv file as current date
    date = datetime.now().strftime("%d-%b-%Y")
    data.to_csv(f'../Covid-19-Api/Datasets/{date}.csv')
    
     # Save last update time to a folder
    now = datetime.now().strftime("%H:%M:%S on %dth of %B 2020")
    file = open("../Covid-19-Api/Datasets/Readme.md", "w")
    file.write(f'File automatically updated at {now}.')
    file.close()

# Run at 6hr intervals
while True:
    fetch()
    tim = datetime.now().strftime("%a %I %p")
    print(f'\n\nLast executed at {tim}... Next execution after 6 hours\n\n\n')
    auto.git()
    print("\n\n\n\nCommitted to Github\n")
    time.sleep(60*60*6)
