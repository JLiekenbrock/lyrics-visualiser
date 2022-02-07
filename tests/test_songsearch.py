from components import songsearch

import lyricsgenius

genius = songsearch.geniuslyrics()



def test_session():
    """Artist
    Test the session
    """
    assert isinstance(genius.get_session(), lyricsgenius.genius.Genius)

test_session()

def test_search_artist(Artist):
    """
    Test the set_artist method
    """
    genius.search_artist(Artist)
    assert genius.get_artist() == Artist
    assert genius.get_artistinstance() is not None

test_search_artist("The Beatles")

def test_search_title(Title):
    """
    Test the set_title method
    """
    genius.search_title(Title)
    assert genius.get_title() == Title

test_search_title("Let It Be")

def test_songsearch_init():
    """
    Test the songsearch class
    """
    s = songsearch.SongSearch()
    assert s.search_results == []
    assert s.search_term == ""

songsearch.find_song("", "")

genius.get_sessioninfo()

genius = lyricsgenius.Genius("u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1")

artist=genius.search_artist("ahhhhhhhhh", max_songs=1)

type(artist)

