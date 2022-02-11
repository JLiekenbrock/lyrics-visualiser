from components import nlp
import numpy as np
import pandas as pd
from pandas import testing as tm

testlyrics = open('./tests/testdata/testsong.txt').read()
testlyricsclean = pd.read_pickle("tests/testdata/testsongclean")
testlyricsdist = np.load("tests/testdata/distances.npy")

def test_clean_lyrics():
    tm.assert_series_equal(nlp.clean_lyrics(testlyrics), testlyricsclean)

def test_distances():
    np.testing.assert_array_equal(nlp.distances(testlyricsclean), testlyricsdist)
