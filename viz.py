import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import numpy as np
import pandas as pd
import random
from matplotlib.pyplot import cm
import plotly.figure_factory as ff
import plotly.graph_objs as go

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='CodeShield'),

    html.Div(children='''
        ML to autoclose False Positive in Anti-Money Laundering
    '''),
])

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(
                    'CodeShield',
                    className='eight columns',
                ),
                html.Img(
                    src="https://d335ljkm83hr4q.cloudfront.net/images/d/dbs-deals_logo_4.png",
                    className='one columns',
                    style={
                        # 'height': '100',
                        # 'width': '225',
                        'float': 'right',
                        # 'position': 'relative',
                    },
                ),
                html.H2(
                    'ML to autoclose False Positive in Anti-Money Laundering'
                ),
            ],
            className='row'
        ),
        html.Div(
            [
                html.H5(
                    '',
                    id='well_text',
                    className='two columns'
                ),
                html.H5(
                    '',
                    id='production_text',
                    className='eight columns',
                    style={'text-align': 'center'}
                ),
                html.H5(
                    '',
                    id='year_text',
                    className='two columns',
                    style={'text-align': 'right'}
                ),
            ],
            className='row'
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id='main_graph')
                    ],
                    className='eight columns',
                    style={'margin-top': '20'}
                ),
                html.Div(
                    [
                        dcc.Graph(id='individual_graph')
                    ],
                    className='four columns',
                    style={'margin-top': '20'}
                ),
            ],
            className='row'
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(id='count_graph')
                    ],
                    className='four columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        dcc.Graph(id='pie_graph')
                    ],
                    className='four columns',
                    style={'margin-top': '10'}
                ),
                html.Div(
                    [
                        dcc.Graph(id='aggregate_graph')
                    ],
                    className='four columns',
                    style={'margin-top': '10'}
                ),
            ],
            className='row'
        ),
    ],
    className='ten columns offset-by-one'
)

if __name__ == '__main__':
    app.run_server(debug=True)
