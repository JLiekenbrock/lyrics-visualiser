# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_table


import lyricsgenius
import re
import numpy as np
import nltk

import plotly

import plotly.express as px

genius = lyricsgenius.Genius("u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1")

artist = genius.search_artist("The Beatles", max_songs=1)
song = artist.song("Let It Be")

# clean lyrics
song = re.sub("[$[*&?].*[$]*&?]", '', song.lyrics)
song = re.sub("EmbedShare.*", '', song)
song = song.replace("\n\n\n", "\n")
song = song.replace("\n\n", "\n").lstrip("\n")

lyrics = song.replace(',', '')
lyrics = lyrics.splitlines()
lyrics[-1]=re.sub('[0-9]+', '', lyrics[-1])

song = song.splitlines()
song[-1]=re.sub('[0-9]+', '', song[-1])

# calculate distance-matrix
lines = [line.split() for line in song]
lines = [x for x in lines if x]

l=len(lines)

d = np.zeros(shape=[l,l])

for i,line in enumerate(lines):
    for j, line2 in enumerate(lines):
        d[i,j] = 1-nltk.jaccard_distance(set(line), set(line2))

# plot result
fig = px.imshow(d,title="Jaccard index between lyric lines")

fig.show()


df = pd.DataFrame(data=song,columns=["lines"]).groupby("lines").size().reset_index(name='size').sort_values(by=["size","lines"],ascending=False)

app = dash.Dash(__name__)
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(children=[
    html.H1(children='Lyrics Visualiser'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

    

