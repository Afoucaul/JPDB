# Author : Armand FOUCAULT

class Word :
	def __init__(self, kanjis=[], kanas="", meanings=[], studiedTimes=0) :
		# list of InWordKanji objects
		self.kanjis = kanjis
		# string ; the word in kanas
		self.kanas = kanas
		# list of strings ; the meanings of the word
		self.meanings = meanings
		# int ; the number of times the word has been studied
		self.studiedTimes = studiedTimes
	
	# add to the meanings of the word a list of meanings
	def addMeaning(self, meanings=[]) :
		for m in meanings :
			self.meanings.append(m)
	
	# remove from the meanings of the word a list of meanings
	def removeMeanings(self, meanings=[]) :
		for m in meanings :
			if m in self.meanings :
				self.meanings.remove(m)
				
	# increments the number of times the word has been studied
	def study(self) :
		self.studiedTimes += 1