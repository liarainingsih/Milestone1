import datetime

from pandas._config.config import options
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import dash_bootstrap_components as dbc
from app import app

external_stylesheets = [dbc.themes.LUX]
 

df = pd.read_csv('supermarket.csv')

layout = html.Div(children=[
    dbc.Row([
        dbc.Col(
            html.H4(children='Visualising Sales per Month'), style={'text-align': 'center'},
            className="mb-4"
            )
        ]),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='month-slider',
        min =  pd.DatetimeIndex(df['Date']).month.min(),
        max = pd.DatetimeIndex(df['Date']).month.max(),
        value = pd.DatetimeIndex(df['Date']).month.min(),
        marks={str(date): str(date) for date in pd.DatetimeIndex(df['Date']).month.unique()},
        step=None
    ),
    
    dbc.Row([
        dbc.Col(
            html.H4(children=''), style={'text-align': 'center'},
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H4(children='Visualising Sales per Hour'), style={'text-align': 'center'},
            className="mb-4"
            )
        ]),
    dcc.Graph(id='graph-with-slider-hour'),
    dcc.Slider(
        id='hour-slider',
        min =  pd.DatetimeIndex(df['Time']).hour.min(),
        max = pd.DatetimeIndex(df['Time']).hour.max(),
        value = pd.DatetimeIndex(df['Time']).hour.min(),
        marks={str(date): str(date) for date in pd.DatetimeIndex(df['Time']).hour.unique()},
        step=None
    )
])

@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('month-slider', 'value'))
def update_figure(selected_time):
    filtered_df = df[pd.DatetimeIndex(df['Date']).month == selected_time]
 
    fig = px.scatter(filtered_df, x="Product line", y="Total",
                      color="Branch", hover_name="City",
                     log_x=False, size_max=55)
 
    fig.update_layout(transition_duration=500)
 
    return fig

@app.callback(
    Output('graph-with-slider-hour', 'figure'),
    Input('hour-slider', 'value'))
def update_figure_hour(selected_time):
    filtered_df = df[pd.DatetimeIndex(df['Time']).hour == selected_time]
 
    fig = px.scatter(filtered_df, x="Product line", y="Total",
                      color="Branch", hover_name="City",
                     log_x=False, size_max=55)
 
    fig.update_layout(transition_duration=500)
 
    return fig
