# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import dash, dcc, html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate

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
        html.Button('Click Me', id='button'),
        html.H3(id='button-clicks'),

        html.Hr(),

        html.Label('Input 1'),
        dcc.Input(id='input-1'),

        html.Label('Input 2'),
        dcc.Input(id='input-2'),

        html.Button(id='button-2'),

        html.Div(id='output')
    ])

    dcc.Graph(
        id='example-graph',
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in repitions.columns],
        data=repitions.to_dict('records'),
    ),

    dcc.Store(id='intermediate-value')
])

@app.callback(Output('intermediate-value', 'data'), Input())

def get_lyrics(value):
    song = songsearch.find_song("dummy", "dummy")
    lyrics = nlp.clean_lyrics(song)

    return lyrics.to_json(date_format='iso', orient='split')

@app.callback(Output('graph', 'figure'), Input('intermediate-value', 'data'))
def update_graph(jsonified_cleaned_data):

    # more generally, this line would be
    # json.loads(jsonified_cleaned_data        figure=visualisation.heatmap(distances)

    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    
    figure=visualisation.heatmap(distances)

    figure = create_figure(dff)
    return figure

@app.callback(Output('table', 'children'), Input('intermediate-value', 'data'))
def update_table(jsonified_cleaned_data):
    dff = pd.read_json(jsonified_cleaned_data, orient='split')
    table = create_table(dff)
    return table


if __name__ == '__main__':
    app.run_server(debug=True)

    

