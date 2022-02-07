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
    html.Button('Click Me', id='button'),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
    ),
    dcc.Store(id='intermediate-value')
])

@app.callback(Output('intermediate-value', 'data'), Input('button', 'value'))
def get_lyrics(value):
    s = songsearch.find_song("dummy", "dummy")
  
    return json.dumps(s)

@app.callback(Output('example-graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):

    lyrics = nlp.clean_lyrics(json.loads(jsonified_cleaned_data))
    distances = nlp.distances(lyrics)
    # more generally, this line would be
    # json.loads(jsonified_cleaned_data        figure=visualisation.heatmap(distances)
    
    figure=visualisation.heatmap(distances)

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)

    

