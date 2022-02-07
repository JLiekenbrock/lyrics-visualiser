# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import dash, dcc, html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import json 
import dash
import dash_table
from components import songsearch
from components import nlp
from components import visualisation

import pandas as pd

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H1(children='Lyrics Visualiser'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    html.Div([

        html.Label('Artist:'),
        dcc.Input(id='artist'),

        html.Label('Songtitle:'),
        dcc.Input(id='songtitle'),

        html.Button('Search Lyrics!', id='search',n_clicks=0),
    ]),

    dcc.Graph(
        id='example-graph',
    ),
    dcc.Store(id='intermediate-value')
])

@app.callback(
    Output('intermediate-value', 'data'), 
    Input('search', 'n_clicks'),
    State("artist", "value"),
    State("songtitle", "value"),
)
def get_lyrics(search,artist,songtitle):

    if artist is not None or "" and songtitle is not None or "":
        songtitle = songtitle
        artist = artist
        s = songsearch.find_song(artist, songtitle)
        return json.dumps(s)
    else:
        return json.dumps("no data here")

@app.callback(Output('example-graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):
    if jsonified_cleaned_data is not None:
        lyrics = nlp.clean_lyrics(json.loads(jsonified_cleaned_data))
        distances = nlp.distances(lyrics)    
        figure=visualisation.heatmap(distances)
        return figure
    else:
        return None
    # more generally, this line would be
    # json.loads(jsonified_cleaned_data        figure=visualisation.heatmap(distances)n figure

if __name__ == '__main__':
    app.run_server(debug=True)

    

