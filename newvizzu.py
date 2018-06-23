import dash
import pandas as pd
import plotly.graph_objs as go 
import dash.dependencies as ddp
import dash_core_components as dcc
import dash_html_components as html


import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import matplotlib.mlab as mlab 
import numpy as np 
import plotly.plotly as py
import geopy
import pickle
import geoloc
import pandas as pd
import base64
import pickle


from geopy.geocoders import Nominatim
geolocator = Nominatim()
#########################################################
def writePickle(var, filename):
    with open(filename, 'wb') as f:  # Python 3: open(..., 'wb')
        pickle.dump(var, f)
        return
 
def readPickle(filename):
    with open(filename, 'rb') as f:  # Python 3: open(..., 'rb')
        return pickle.load(f)



master = readPickle('data/master.pkl')[0]
m = geoloc.setBaseplot()


second = 1000
minute = 60
hour   = 60
day    = 24
interval = 1/2*day*hour*minute*second

def plot_figure(data):
    layout = dict(
        title="Figure w/ plotly",
    )

    fig = dict(data=data, layout=layout)
    return fig

def gen_plot():
    df=pd.read_csv('data/CSSol-2/whole_train.csv')
    df=df[['ordering_customer','beneficiary']].reset_index()
    df=df.astype('str')
    row = df.iloc[[0]]
    fromcity, tocity, fromtuple, totuple = geoloc.updateLatLong(row, master, geolocator)
    fig = geoloc.plotGeoPlot(m, fromcity, tocity, fromtuple, totuple)
    
    return fig

def serve_layout():
    return html.Div(children=[
        html.Div([
            html.H1("Plotly test with Live update",
                    style={"font-family": "Helvetica", 
                           "border-bottom": "1px #000000 solid"}),
            ], className='banner'),
        html.Div([dcc.Graph(id='plot', figure=gen_plot())],),
        dcc.Interval(id='live-update', interval=interval),
],)

app = dash.Dash()

app.layout = serve_layout

app.callback(
    ddp.Output('plot', 'figure'),
    [],
    [],
    [ddp.Event('live-update', 'interval')])(gen_plot)

if __name__ == '__main__':
    app.run_server(debug=True)
