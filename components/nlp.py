import pandas as pd
import numpy as np
import nltk
import re

# clean lyrics
def clean_lyrics(rawlyrics):

    song = re.sub("[$[*&?].*[$]*&?]", '', rawlyrics)
    song = re.sub("EmbedShare.*", '', song)
    song = song.replace("\n\n\n", "\n")
    song = song.replace("\n\n", "\n").lstrip("\n")

    # for removing commas if necessary
    #song = song.replace(',', '')

    song = song.splitlines()
    song[-1] = re.sub('[0-9]+', '', song[-1])

    return song

# calculate distances
def distances(cleanlyrics):
    # calculate distance-matrix
    lines = [line.split() for line in cleanlyrics]
    lines = [x for x in lines if x]

    l=len(lines)

    d = np.zeros(shape=[l,l])

    for i,line in enumerate(lines):
        for j, line2 in enumerate(lines):
            d[i,j] = 1-nltk.jaccard_distance(set(line), set(line2))    
    return d

# calculate repititions
def repitiontable(song):
    repitions = pd.DataFrame(data=song,columns=["lines"]).\
        groupby("lines").\
        size().\
        reset_index(name='size').\
        sort_values(by=["size","lines"],ascending=False)

    return repitions