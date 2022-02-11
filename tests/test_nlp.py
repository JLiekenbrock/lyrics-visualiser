from components import nlp
from components import visualisation
from scipy.spatial.distance import pdist, jaccard

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
import nltk
import re

testlyrics = open('./tests/HeyJude.txt').read()

testlyrics

def clean_lyrics(rawlyrics):
    return pd.Series(testlyrics).\
        str.replace("[$[*&?].*[$]*&?]", '', regex = True).\
        str.replace("EmbedShare.*", '', regex = True).\
        str.replace("Embed*", '', regex = True).\
        str.replace("\n\n\n", "\n").\
        str.replace("\n\n", "\n").\
        str.replace('[0-9]+', '',regex= True).\
        str.split("\n").\
        explode(ignore_index=True)

lyrics = clean_lyrics(testlyrics)

lyrics.to_json()

pd.read_json(lyrics.to_json(), typ='series') == lyrics

d.values[[2]]

def distances(cleanlyrics):
    d = np.zeros(shape=[cleanlyrics.size,cleanlyrics.size])
    for i,line in enumerate(cleanlyrics):
        for j, line2 in enumerate(cleanlyrics):
            d[i,j] = 1-nltk.jaccard_distance(set(line), set(line2))    
    return d

d = np.zeros(shape=[clean.size,clean.size])
d
for i,line in enumerate(cleanlyrics):
    for j, line2 in enumerate(cleanlyrics):
        d[i,j] = 1-nltk.jaccard_distance(set(line), set(line2))    


distance(d.values[[2]])