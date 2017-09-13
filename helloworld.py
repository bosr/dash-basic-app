import dash
import dash_html_components as html
import dash_core_components as dcc

my_app = dash.Dash('my app')

my_app.layout = html.Div([
    html.H1('Hello PlotCon'),
    html.Label('Stock Tickers'),
    dcc.Input(
        value='TLSA',
        id='my-input'),
    dcc.Graph(
        id='my-graph',
        figure={
            'data': [
                {'x': [1, 2], 'y': [3, 1]}
            ]
        }
    )
])

my_app.server.run(debug=True)
