# Author : Armand FOUCAULT

class InWordKanji(Kanji) :
	def __init__(self, character, meanings=[], strokes=0, position=0) :
		Kanji.__init__(character, meanings, strokes)
		# an int that represents the position of the kanji in 
		self.position = position