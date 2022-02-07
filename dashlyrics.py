# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dash, dcc, html, dash_table
from dash.dependencies import Output, Input, State
import json 

from components import songsearch
from components import nlp
from components import visualisation

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
    if artist not in [None, ""] and songtitle not in [None,""]:
        new_artist = artist
        new_songtitle = songtitle
        s = songsearch.find_song(new_artist, new_songtitle)
        lyrics = nlp.clean_lyrics(s)
        return json.dumps(lyrics)
    else:
        return json.dumps("no data here")

@app.callback(Output('example-graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):
    if jsonified_cleaned_data is not None:
        lyrics = json.loads(jsonified_cleaned_data)
        distances = nlp.distances(lyrics)    
        figure = visualisation.heatmap(distances)
        return figure
    else:
        return None

if __name__ == '__main__':
    app.run_server(debug=True)

    

