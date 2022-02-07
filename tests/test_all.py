from components import songsearch
from components import nlp
import visualisation

s = songsearch.find_song("dummy", "dummy")

t=nlp.clean_lyrics(s)


