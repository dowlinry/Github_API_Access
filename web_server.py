from flask import Flask, render_template, url_for

import plotly
import plotly.graph_objs as go

import pandas as pd
import numpy as np
import json

web_server = Flask(__name__)

@web_server.route('/')
def index():
    return render_template('index.html')

if  __name__ == '__main__':
    web_server.run(debug=True)
