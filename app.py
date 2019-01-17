import csv

from flask import Flask
from flask import request
import requests

app = Flask(__name__)


@app.route("/")
def index():
    response = requests.get('http https://swapi.co/api/')
    data = response.json()

    print(data[results])


    index_file = open('index.html', 'r')
    index_html = index_file.read()
    index_html = index_html.replace('{{planet_list}}', planet_html)

    index_file.close()

    return index_html
