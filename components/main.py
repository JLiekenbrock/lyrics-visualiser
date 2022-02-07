import songsearch
import nlp

song = songsearch.find_song("dummy", "dummy")

processed = nlp.clean_lyrics(song)

distances = nlp.distances(processed)