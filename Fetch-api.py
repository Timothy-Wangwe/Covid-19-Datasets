#______________
#Timothy Wangwe
#==============

# Import 3rd party libraries
import urllib.request
import json
import pandas as pd
from datetime import datetime
import time

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
    name = datetime.now().strftime("%d-%b-%Y")
    data.to_csv(f'Data-Sets/{name}.csv')

     # Save last update time to a folder
    update = datetime.now().strftime("%H:%M:%S on %dth %b")
    file = open("Data-Sets/Data-update.txt", "w")
    file.write(f'File last updated at {update}')
    file.close()

# Automate Github updates
def git():
    from os import system

    system("git pull")
    system("git add *")
    system("git commit -m 'Automated hourly dataset update'")
    system("git push")
    system("git status")

# Run after every 1hr
while True:
    fetch()
    tim = datetime.now().strftime("%a %I %p")
    print(f'\n\nLast executed at {tim}... Next execution after 1 hour\n\n\n')
    git()
    print("\n\n\n\nCommitted to Github\n")
    time.sleep(60*60)
