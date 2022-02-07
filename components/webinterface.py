# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import songsearch
import nlp
import visualisation

app = dash.Dash(__name__)
server = app.server

song = songsearch.find_song("dummy", "dummy")
lyrics = nlp.clean_lyrics(song)
distances = nlp.distances(lyrics)
repitions = nlp.repitiontable(lyrics)

app.layout = html.Div(children=[
    html.H1(children='Lyrics Visualiser'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=visualisation.heatmap(distances)
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in repitions.columns],
        data=repitions.to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

    

