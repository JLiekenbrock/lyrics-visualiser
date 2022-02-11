from threading import get_ident
from components import geniuswrapper
from components import nlp

genius = geniuswrapper.geniuslyrics()

testsong = genius.search_lyrics("Hey Jude","The Beatles")

testsongclean = nlp.clean_lyrics(testsong)

with open("tests/testsong.txt", 'w') as f:
    f.write(testsong)

with open("tests/testsongclean.txt", 'w') as f:
    f.write(str(nlp.clean_lyrics(testsong)))

with open("tests/distances.txt", 'w') as f:
    f.write(str(nlp.distances(testsongclean)))
