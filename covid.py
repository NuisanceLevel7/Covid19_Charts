#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template
from App import app
import sys
import json


def GenCharts():
    daily_deaths = '/home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/owid-covid-data.json'
    with open(daily_deaths) as json_file:
        covid_data = json.load(json_file)

    DATA = dict()
    DATA['dates'] = list()
    DATA['deaths'] = list()
    DATA['deaths7d'] = list()
    DATA['cases'] = list()
    DATA['cases7d'] = list()
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

    DATA['cases7d'] = compute7d(DATA['cases'])
    cases7d =   ','.join(DATA['cases7d'])
    cases7d =   '[' + cases7d + ']'

    DATA['deaths7d'] = compute7d(DATA['deaths'])
    deaths7d =   ','.join(DATA['deaths7d'])
    deaths7d =   '[' + deaths7d + ']'


    with app.app_context():
        data = render_template("covid_chart1.html",deaths=deaths,dates=dates,cases=cases,
                                 totalcases=total_cases,totaldeaths=total_deaths,cases7d=cases7d,deaths7d=deaths7d)
    print(data)

def compute7d(arraydata):
    N = 7
    cumsum, moving_aves = [0], []

    for i, x in enumerate(arraydata, 1):
        x = int(float(x))
        cumsum.append(cumsum[i-1] + x)
        if i>=N:
            moving_ave = (cumsum[i] - cumsum[i-N])/N
            #can do stuff with moving_ave here
            moving_aves.append(str(int(moving_ave)))
        else:
            moving_aves.append(str(x))
    return moving_aves

def main():
    GenCharts()

# Boiler plate call to main()
if __name__ == '__main__':
  main()
                    
               
sys.exit()


