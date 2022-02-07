import lyricsgenius

def find_song(artist, song):
    genius = lyricsgenius.Genius("u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1")

    artist = ""
    song = ""
    
    while True:
        try:
            artist = genius.search_artist("The Beatles", max_songs=1)
            song = artist.song("Let It Be")
            break
        except:
            pass

    return song.lyrics
