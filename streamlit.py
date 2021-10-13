import streamlit as st
import lyricsgenius
import re
import numpy as np
import plotly.express as px
import nltk

# get lyrics from genius.com 
genius = lyricsgenius.Genius("insert token")

with st.form(key='form'):
    artist_input = st.text_input("artist", "The Beatles")
    song_input = st.text_input("song", "Let It Be")
    submit_button = st.form_submit_button(label='Get Lyrics from Genius.com')

artist = genius.search_artist(artist_input, max_songs=1)
song = artist.song(song_input)

# clean lyrics
song = re.sub("[$[*&?].*[$]*&?]", '', song.lyrics)
song = re.sub("EmbedShare.*", '', song)
song = song.replace("\n\n\n", "\n")
song = song.replace("\n\n", "\n").lstrip("\n").replace(',', '')
song = song.splitlines()
song[-1]=re.sub('[0-9]+', '', song[-1])

# calculate distance-matrix
lines = [line.split() for line in song]

l=len(lines)

d = np.zeros(shape=[l,l])

for i,line in enumerate(lines):
    for j, line2 in enumerate(lines):
        d[i,j] = 1-nltk.jaccard_distance(set(line), set(line2))

# plot result
fig = px.imshow(d,title="Jaccard index between lyric lines")
st.plotly_chart(fig)

''' experimental: network-graph
from stvis import pv_static
from pyvis.network import Network
import networkx as nx
G = nx.DiGraph(d)
g = Network("500px","500px")
g.from_nx(G)
pv_static(g)
'''


