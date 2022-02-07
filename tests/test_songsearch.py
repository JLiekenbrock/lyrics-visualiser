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
    Test the search_artist method
    """
    genius.search_artist(Artist)
    assert genius.get_artist() == Artist
    assert genius.get_artistinstance() is not None

test_search_artist("The Beatles")

def test_search_artist_invalid(Artist):
    """
    Test the search_artist method
    """
    genius.search_artist(Artist)
    assert genius.get_artist() == Artist
    assert genius.get_artistinstance() is None

test_search_artist_invalid("")

def test_search_lyrics(title,artist):
    """
    Test the set_title method
    """
    genius.search_lyrics(title,artist)
    assert type(genius.get_lyrics()) == str

test_search_lyrics("Let It Be","The Beatles")

def test_search_lyrics_invalid(title,artist):
    """
    Test the set_title method
    """
    genius.search_lyrics(title,artist)
    assert type(genius.get_lyrics()) == None

test_search_lyrics_invalid("","The Beatles")