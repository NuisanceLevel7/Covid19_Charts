#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template
from App import app
import sys,time,datetime
from Tools import Files

def UpdateLogPage():
 
    f = Files()
    f.read_file('/var/www/html/updater.log')
    with app.app_context():
        html = render_template("covid_logview.html",log=list(reversed(f.data)))

    print(html)

def main():
    UpdateLogPage()

# Boiler plate call to main()
if __name__ == '__main__':
  main()
                    
sys.exit()


