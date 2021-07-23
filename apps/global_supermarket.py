import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
external_stylesheets = [dbc.themes.LUX]
 
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
 
# Data Preprocessing
df = pd.read_csv('supermarket.csv')
df.drop(['Invoice ID', 'Branch', 'Customer type', 'Gender',
       'Product line', 'Unit price', 'Quantity', 'Tax 5%', 'Date',
       'Time', 'Payment', 'cogs', 'gross margin percentage', 'gross income',
       'Rating'], axis=1, inplace=True)
df.set_index('City', inplace=True)
dfT = df.T
 
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Visualising Supermarket Sales'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': city, 'value': city} for city in dfT.columns.unique()
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='main-graph'
                )
            )
        ])
    ])
])
 
@app.callback(
    Output('main-graph', 'figure'),
    Input('selected_city', 'value')
)
def update_chart(city):
    fig = px.line(dfT, x=dfT.index, y=city)
    return fig
 