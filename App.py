#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

# This is just the minimum flask framework needed to use render_template in a standalone script.
# This project uses render_template to create static pages with charts of covid data,

@app.route('/')
def hello():
    return "Hello World!"
