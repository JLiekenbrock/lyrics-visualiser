from components import geniuswrapper
from components import nlp
import numpy as np

genius = geniuswrapper.geniuslyrics()

testsong = genius.search_lyrics("Hey Jude","The Beatles")

with open("tests/testsong.txt", 'w') as f:
    f.write(testsong)

testsongclean = nlp.clean_lyrics(testsong)

testsongclean.to_pickle("tests/testsongclean")

np.save("tests/distances.npy",nlp.distances(testsongclean))

