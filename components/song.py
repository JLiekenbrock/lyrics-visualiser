class Car():
	brand = "Tesla"
	color = "Red"
	kind = "Sedan"

	def __str__(self):
		return "Car=>" + "[" + self.brand + ","+ self.color + "," + self.kind + "]"

	def setBrand(self, aBrand):
		self.brand = aBrand
		return self

	def setColor(self, aColor):
		self.color = aColor
		return self

	def setKind(self, aKind):
		self.kind = aKind
		return self

car = Car()
car.setBrand("BMW").setColor("Blue").setKind("Mni") 

print("Print Cars...")
print(car)

import lyricsgenius

session = lyricsgenius.Genius("u41cjDZINLUj4yX8g6x-4BaejLoZtqel0vN-jEsXag4gjfp85C9NA0oxzaf9Oxk1")

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

song = Song()

song.setArtist("The Beatles").setTitle("Hey Jude")

print(song)