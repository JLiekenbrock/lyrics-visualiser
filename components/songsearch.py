import lyricsgenius

def find_song(artist, title):
    genius = lyricsgenius.Genius("u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1")
    
    art = artist
    tit = title
    while True:
        try:
            artist = genius.search_artist(art, max_songs=1)
            song = artist.song(tit)
            break
        except:
            pass

    return song.lyrics
