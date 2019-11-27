
from plotly.offline import plot
from graph import Graph 

gp = Graph('results.json','languages.json')
fig = gp.create_graph()
plot(fig)

