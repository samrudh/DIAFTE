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
import random


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
m , imgplot= geoloc.setBaseplot()


# pip install pyorbital
from pyorbital.orbital import Orbital
satellite = Orbital('TERRA')

image_filename = '/Users/kirankunapuli/Documents/GitHub/DIAFTE/data/pic.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app = dash.Dash(__name__)
app.layout = html.Div(
    html.Div([
        html.H1('CodeShield- Team DIAFTE'),
        html.H3('ML to autoclose False Positive in Anti-Money Laundering'),
        html.Div(id='live-update-text'),
        # html.Img(
        #     src="https://d335ljkm83hr4q.cloudfront.net/images/d/dbs-deals_logo_4.png",
        #     className='one columns',
        #     style={
        #         # 'height': '100',
        #         # 'width': '225',
        #         # 'float': 'right',
        #         # 'position': 'relative',
        #     },
        # ),
        
        html.Img(id='live-update-graph',src='data:data;base64,{}'.format(encoded_image.decode()), className='one columns'),
        # html.Div(id='live-update-graph'),

        dcc.Interval(
            id='interval-component',
            interval=10*1000, # in milliseconds
            n_intervals=0
        )
    ])
)


@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_metrics(n):
    lon, lat, alt = satellite.get_lonlatalt(datetime.datetime.now())
    style = {'padding': '5px', 'fontSize': '16px'}
    return [
        html.Span('Latest Swift message was : {0:.2f}'.format(lon), style=style)
       
    ]


# Multiple components can update everytime interval gets fired.
@app.callback(Output('live-update-graph', 'children'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    
    df=pd.read_csv('data/CSSol-2/whole_train.csv')
    df=df[['ordering_customer','beneficiary']].reset_index()
    df=df.astype('str')
    row = df.iloc[[random.randint(1,15)]].reset_index()
    fromcity, tocity, fromtuple, totuple = geoloc.updateLatLong(row, master, geolocator)
    fig = geoloc.plotGeoPlot(m, fromcity, tocity, fromtuple, totuple, imgplot)
    return fig
    # html_txt = '<img src="/Users/kirankunapuli/Documents/GitHub/DIAFTE/data/pic.png" alt="GeoMap Visualization">'
    # return [html.H2('GeoMap Image')]






# def update_graph_live(n):
#     satellite = Orbital('TERRA')
#     data = {
#         'time': [],
#         'Latitude': [],
#         'Longitude': []
#     }

#     # Collect some data
#     for i in range(180):
#         time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
#         lon, lat, alt = satellite.get_lonlatalt(
#             time
#         )
#         data['Longitude'].append(lon)
#         data['Latitude'].append(lat)
#         data['time'].append(time)

#     # Create the graph with subplots
#     fig = plotly.tools.make_subplots(rows=2, cols=1, vertical_spacing=0.2)
#     fig['layout']['margin'] = {
#         'l': 30, 'r': 50, 'b': 50, 't': 50
#     }
#     fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

#     fig.append_trace({
#         'x': data['Longitude'],
#         'y': data['Latitude'],
#         'text': data['time'],
#         'name': 'Longitude vs Latitude',
#         'mode': 'lines+markers',
#         'type': 'scatter'
#     }, 1, 1)

#     return fig


if __name__ == '__main__':
     app.run_server(port=8057, debug=True)
     app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
