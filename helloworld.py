import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas_datareader as pdr

my_app = dash.Dash('my app')

my_app.layout = html.Div([
    html.H1('Hello PlotCon'),
    html.Label('Stock Tickers'),
    dcc.Input(
        value='AAPL',
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


# update my-graph any time my-input changes
@my_app.callback(
    Output(component_id='my-graph', component_property='figure'),
    [Input(component_id='my-input', component_property='value')])
def update_graph(stock_ticker):
    # stock_ticker = stock_ticker_input.value
    print(stock_ticker)
    df = pdr.get_data_yahoo(stock_ticker.strip('\n'))
    figure = {
        'data': [
            {
                'x': df.index,
                'y': df.Open
            }
        ]
    }
    # returned value is merged in the 'my-graph' component
    return figure

my_app.server.run(debug=True)
