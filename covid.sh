#!/bin/bash

echo "`date` - Updating cofid data repo"
rm -r /home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/*

cd /home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/
wget https://github.com/owid/covid-19-data/raw/master/public/data/owid-covid-data.json
wget https://api.covidtracking.com/v1/us/current.json


echo "`date` - Updating Charts"
cd /home/vengle/Projects/covid19/App
./covid.py > /var/www/html/covid.html
echo "`date` - Update Complete."
cat /var/www/html/updater.log |tail -100 >/tmp/covidlog
cat /tmp/covidlog > /var/www/html/updater.log 
./logpage.py >  /var/www/html/covid_logview.html
