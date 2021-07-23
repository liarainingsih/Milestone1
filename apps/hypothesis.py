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
            html.H4(children='Hypothesis Sales'), style={'text-align': 'center'},
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H5(children='Chi Square Test'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Uji Chi-square yang umum dikenal oleh banyak orang adalah pengujian terhadap keterkaitan antara dua buah variabel hasil perhitungan (count data), sehingga dasar pengujian yang digunakan adalah selisih nilai proporsi dari nilai observasi dengan nilai harapan. '),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Nilai Observed chi2: 11.56'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Nilai p-value: 0.3156'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Kesimpulan : H0 diterima. Tidak ada hubungan antara City dengan pembelian line'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H5(children='Two Sample Test'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Hubungan antara Product line : Fashion accessories dan Food beverages.'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Fashion accessories sample mean : 305.089'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Fashion accessories sample std : 243.564'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Fashion accessories sample Kurtosis : 0.353'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='Food beverages sample mean : 322.672'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='t-statistik : 0.672'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.P(children='p-value : 0.251'),
            className="mb-4"
            )
        ]),
    dbc.Row([
        dbc.Col(
            html.H6(children='Kesimpulan : Nilai p-value > 0.05 H0 diterima.'),
            className="mb-4"
            )
        ])
])
