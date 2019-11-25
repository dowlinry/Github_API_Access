from flask import Flask, render_template, url_for

import plotly
import plotly.graph_objs as go


from graph import Graph 
import json

web_server = Flask(__name__)
gp = Graph('results.json')
gp.create_graph()

@web_server.route('/')
def index():
    return render_template('index.html')

if  __name__ == '__main__':
    web_server.run(debug=True)
