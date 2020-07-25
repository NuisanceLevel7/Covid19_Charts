#!/bin/bash

cd /home/vengle/Projects/covid19/ourworld/covid-19-data/public/data/
git status
git pull

cd /home/vengle/Projects/covid19/App
./covid.py > /var/www/html/covid.html
