import dash_html_components as html
import dash_bootstrap_components as dbc

 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("My Name is Lia, student Hacktiv 8 Data Science",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='MILESTONE 1'),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children='Supermarket Sales Dashboard'),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the dashboard here',
                        className="text-center"),
                        dbc.Button("Supermarket Sales Dataset",
                        href="apps/slider_supermarket",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit my Github Page',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/liarainingsih",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])