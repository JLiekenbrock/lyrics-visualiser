from components import nlp

testlyrics = open('./tests/testsong.txt').read()
testlyricsclean = open('./tests/testsongclean.txt').read()
testlyricsdist = open('./tests/distances.txt').read()

testlyricsclean
testlyricsdist

nlp.distances(nlp.clean_lyrics(testlyrics))

s.to_pickle('filename')

and

s = pd.read_pickle('filename')

def test_clean_lyrics():
    assert str(nlp.clean_lyrics(testlyrics)) == testlyricsclean

#def test_distances():
#    assert str(nlp.distances(testlyricsclean)) == testlyricsdist
