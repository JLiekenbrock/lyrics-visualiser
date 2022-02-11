import pandas as pd
import numpy as np
import nltk

# clean lyrics
def clean_lyrics(rawlyrics):
    return pd.Series(rawlyrics).\
        str.replace("[$[*&?].*[$]*&?]", '', regex = True).\
        str.replace("EmbedShare.*", '', regex = True).\
        str.replace("Embed*", '', regex = True).\
        str.replace("\n\n\n", "\n").\
        str.replace("\n\n", "\n").\
        str.replace('[0-9]+', '',regex= True).\
        str.split("\n").\
        explode()

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

# calculate repititions, not used in current version
def repitiontable(song):
    return pd.DataFrame(data=song,columns=["lines"]).\
        groupby("lines").\
        size().\
        reset_index(name='size').\
        sort_values(by=["size","lines"],ascending=False)