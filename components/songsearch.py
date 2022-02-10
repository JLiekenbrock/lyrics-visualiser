import lyricsgenius


## Interface to the Genius API
class Song():
    artist = ""
    title = ""
    
    def __str__(self):
        return "Song=>" + "[" + self.artist + ","+ self.title+ "]"

    def setArtist(self, anArtist):
        self.artist = anArtist
        return self

    def setTitle(self, aTitle):
        self.title = aTitle
        return self

# If using several lyrics provider this class should be inherited
class geniuslyrics:
    """
    Class for searching for lyrics
    """
    def __init__(self,_token = "u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1",_timeout=15,_retries=3,_verbose=False):
        self.__session = lyricsgenius.Genius(_token,timeout=_timeout,retries=_retries,verbose=_verbose)
        self.__artistname = None
        self.__artistinstance = None
        self.__titlename = None
        self.__titleinstance = None
        self.__lyrics = None

    def get_session(self):
        return self.__session

    def search_artist(self,artist):
        if(artist is not self.__artistname):
            self.__artistname = artist
            self.__artistinstance = self.__session.search_artist(artist, max_songs=1)

    def get_artist(self):
        return self.__artistname

    def get_artistinstance(self):
        return self.__artistinstance

    def search_title(self,title):
        if title is not self.__titlename and self.__artistinstance is not None:
            self.__titlename = title
            self.__titleinstance = self.__artistinstance.song(title)
            self.__set_lyrics()
        else:
            self.__titleinstance = None
            self.__set_lyrics()

    def get_title(self):
        return self.__titlename

    def __set_lyrics(self):
        if self.__titleinstance is not None:
            self.__lyrics = self.__titleinstance.lyrics
        else: 
            self.__lyrics = None

    def get_lyrics(self):
        return self.__lyrics

    def search_lyrics(self,title,artist):
        self.search_artist(artist)
        self.search_title(title)
        return self.get_lyrics()