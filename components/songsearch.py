from components import geniuswrapper

genius = geniuswrapper.geniuslyrics()

## Interface to the api-wrapper. based on the dsl example
class Song():
    artist = ""
    title = ""
    lyrics = ""
    
    def __str__(self):
        return "Song=>" + "[" + self.artist + ","+ self.title+ "]"

    def setArtist(self, anArtist):
        self.artist = anArtist
        return self

    def setTitle(self, aTitle):
        self.title = aTitle
        return self

    def getLyrics(self,provider="Genius"):
        if provider == "Genius":
            return genius.search_lyrics(self.title,self.artist)

