#!/bin/bash


echo "`date` - Updating cofid data repo"
cd /home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/
git status
git pull

echo "`date` - Updating Charts"
cd /home/vengle/Projects/covid19/App
./covid.py > /var/www/html/covid.html
echo "`date` - Update Complete."
./logpage.py >  /var/www/html/covid_logview.html
