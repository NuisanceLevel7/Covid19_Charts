#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template
from App import app
import sys,time,datetime
import json
from Tools import Files



def GenCharts():
    daily_deaths = '/home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/owid-covid-data.json'
    current = '/home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/current.json'
    with open(daily_deaths) as json_file:
        covid_data = json.load(json_file)

    with open(current) as json_file:
        current_data = json.load(json_file)

    hospitalized_curr = current_data[0]['hospitalizedCurrently']
    onVentilatorCurrently = current_data[0]['onVentilatorCurrently']
    last = 0

    DATA = dict()
    DATA['dates'] = list()
    DATA['deaths'] = list()
    DATA['deaths7d'] = list()
    DATA['cases'] = list()
    DATA['cases7d'] = list()
    DATA['hospitalized'] = list()
    for dataset in covid_data['USA']['data']:
        deaths = "0"
        cases = "0"
        hospitalized = "0"
        if "new_deaths" in dataset:
            deaths = str(dataset["new_deaths"])
        if "hosp_patients" in dataset:
            hospitalized  = str(dataset["hosp_patients"])
            last = hospitalized
        else:
            hospitalized = str(last)
        totalhospitalized = int(float(hospitalized_curr))

        date =  dataset["date"]
        if "new_cases" in dataset:
            cases = str(dataset["new_cases"])
        if "total_cases" in dataset:
            total_cases = dataset["total_cases"]
        if "total_deaths" in dataset:
            total_deaths = dataset["total_deaths"]
        DATA['deaths'].append(deaths)
        DATA['cases'].append(cases)
        DATA['hospitalized'].append(hospitalized)
        DATA['dates'].append('"' + date + '"')
        dailycases = cases
        dailydeaths = deaths

    del DATA['hospitalized'][-1]
    DATA['hospitalized'].append(str(hospitalized_curr))
    deaths =  ','.join(DATA['deaths']) 
    deaths = '[' + deaths + ']'

    cases =  ','.join(DATA['cases'])
    cases = '[' + cases + ']'

    hospitalized =  ','.join(DATA['hospitalized'])
    hospitalized = '[' + hospitalized + ']'

    dates =  ','.join(DATA['dates']) 
    dates = '[' + dates + ']'

    total_cases = "{:,}".format(int(total_cases))
    total_deaths = "{:,}".format(int(total_deaths))
    totalhospitalized = "{:,}".format(int(totalhospitalized))
    totalvent = "{:,}".format(int(onVentilatorCurrently))
    dailycases = "{:,}".format(int(float(dailycases)))
    dailydeaths = "{:,}".format(int(float(dailydeaths)))

    DATA['cases7d'] = compute7d(DATA['cases'])
    cases7d =   ','.join(DATA['cases7d'])
    cases7d =   '[' + cases7d + ']'

    DATA['deaths7d'] = compute7d(DATA['deaths'])
    deaths7d =   ','.join(DATA['deaths7d'])
    deaths7d =   '[' + deaths7d + ']'

    now = str(time.strftime('%X %x %Z'))
 
    #f = Files()
    #f.read_file('/var/www/html/updater.log')
 
    #log = ''
    #for line in reversed(f.data):
    #    log += line + "\n"    

    with app.app_context():
        data = render_template("covid_chart1.html",deaths=deaths,dates=dates,cases=cases,
                                 totalcases=total_cases,totaldeaths=total_deaths,cases7d=cases7d,
                                 deaths7d=deaths7d,hospitalized=hospitalized,
                                 totalhospitalized=totalhospitalized,totalvent=totalvent,
                                 dailycases=dailycases,dailydeaths=dailydeaths,now=now)
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


