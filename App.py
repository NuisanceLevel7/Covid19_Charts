#!/home/vengle/Projects/covid19/bin/python3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"
