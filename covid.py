#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template
from App import app
import sys
import json


daily_deaths = '/home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/owid-covid-data.json'
with open(daily_deaths) as json_file:
    covid_data = json.load(json_file)

DATA = dict()
DATA['deaths'] = list()
DATA['dates'] = list()
DATA['cases'] = list()
for dataset in covid_data['USA']['data']:
    deaths = str(dataset["new_deaths"])
    date =  dataset["date"]
    cases = str(dataset["new_cases"])
    total_cases = dataset["total_cases"]
    total_deaths = dataset["total_deaths"]
    DATA['deaths'].append(deaths)
    DATA['cases'].append(cases)
    DATA['dates'].append('"' + date + '"')


deaths =  ','.join(DATA['deaths']) 
deaths = '[' + deaths + ']'

cases =  ','.join(DATA['cases'])
cases = '[' + cases + ']'

dates =  ','.join(DATA['dates']) 
dates = '[' + dates + ']'

total_cases = "{:,}".format(int(total_cases))
total_deaths = "{:,}".format(int(total_deaths))


with app.app_context():
  data = render_template("covid_chart1.html",deaths=deaths,dates=dates,cases=cases,totalcases=total_cases,totaldeaths=total_deaths)


print(data)

