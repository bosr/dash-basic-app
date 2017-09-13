import dash

my_app = dash.Dash('my app')

from dash_html_components import H1, Textarea
from dash_core_components import Graph

my_app.layout = H1('Hello PlotCon')

my_app.server.run(debug=True)
