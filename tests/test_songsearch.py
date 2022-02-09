from components import songsearch

import lyricsgenius

genius = songsearch.geniuslyrics()

def test_session():
    """Artist
    Test the session
    """
    assert isinstance(genius.get_session(), lyricsgenius.genius.Genius)

def test_search_artist():
    """
    Test the search_artist method
    """
    genius.search_artist("The Beatles")
    assert genius.get_artist() == "The Beatles"
    assert genius.get_artistinstance() is not None

def test_search_artist_invalid():
    """
    Test the search_artist method
    """
    genius.search_artist("")
    assert genius.get_artist() == ""
    assert genius.get_artistinstance() is None

def test_search_lyrics():
    """
    Test the set_title method
    """
    genius.search_lyrics("Let It Be","The Beatles")
    assert type(genius.get_lyrics()) == str


def test_search_lyrics_invalid():
    """
    Test the set_title method
    """
    genius.search_lyrics("","")
    assert isinstance(genius.get_lyrics(), type(None))
