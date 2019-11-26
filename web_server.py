from flask import Flask, render_template, url_for

from graph import Graph 
import chart_studio.tools as tls
import plotly.graph_objects as go

web_server = Flask(__name__)
gp = Graph('results.json','languages.json')
fig = gp.create_graph()
df = gp.create_dataframe()


@web_server.route('/')
def index():
    return render_template('temp-plot.html',tables=[df.to_html(classes='data')], titles=df.columns.values)

if  __name__ == '__main__':
    web_server.run(debug=True)
