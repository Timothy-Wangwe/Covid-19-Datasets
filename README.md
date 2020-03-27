# Covid-19-Datasets

Fetching Covid-19 Datasets for all countries from an open [API](https://api.covid19api.com/). The data is saved as csv files and stored in the folder [Data-Sets](Data-Sets).

### Dependecies
We've used [urllib.request](https://docs.python.org/3/library/urllib.request.html#module-urllib.request) which is basically a version of the original package [urllib](https://docs.python.org/3/library/urllib.html) used in [python3](https://docs.python.org/). There is no need for installation if you're using python3.

### Hosting
![Pythonanywhere](https://www.pythonanywhere.com/static/anywhere/images/PA-logo.svg)
### [Notebook](Fetch-api.iypnb)
This notebook gives a step-by-step demonstration of how the data is retrieved, manipulated and stored here. It however requires to be manually run everytime to acquire updated data. For this reason, I recreated an executable python [file](Fetch-api.py) that can work as the notebook would.

### [Python File](Fetch-api.py)
The script in this file is excecuted automatically after every 1 hour(60*60 secs) and the saved files updated.
It however requires to be hosted on an online server for it to keep running. I opted to use a free hosting service on [Python anywhere](pythonanywhere.com), my script is currently running there. You can try other services as you wish.
