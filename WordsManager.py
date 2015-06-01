# Author : Armand FOUCAULT

from Word import *
from Kanji import * # /!\ create a Kanji class, and the KanjiManager that goes along with
from sqlite3 import *

class WordsManager :
	def __init__(self, database, kanjisManager=None) :
		# list of words ; the words the manager has access to
		self.words = []
		# an sqlite3 connection to the database
		self.database = database
		# the KanjisManager
		self.kanjisManager = kanjisManager
		
	def bindKanjisManager(self, kanjisManager) :
		self.kanjisManager = kanjisManager
		
	def constructWord(self, id_word) :
		cursor = self.database.cursor()
		# Getting kanas and studiedTimes for the word
		cursor.execute("""SELECT kanas, studied_times FROM words WHERE id_word = ?""", (id_word,))
		result = cursor.fetchone()[0]
		kanas = result[0]
		studiedTimes = result[1]
		# Getting meanings for the word
		cursor.execute("""SELECT m.meaning FROM meanings AS m INNER JOIN words_meanings AS w_m ON m.id_meaning = w_m.id_meaning WHERE w_m.id_word = ?""", (id_word,))
		meanings = []
		for m in cursor :
			meanings.append(m)
		# Getting the id of the kanjis for the word
		cursor.execute("""SELECT id_kanji, position FROM words_kanjis WHERE id_word = ?""", (id,))
		kanjis = []
		for couple in cursor :
			kanjis.append(constructInWordKanji(id = cursor[0], position = cursor[1]) # /!\ create a InWordKanji class that inherits from Kanji and that has as an attribute a position in a word
		return Word(kanjis = kanjis, kanas = kanas, meanings = meanings, studiedTimes = studiedTimes)
	
	def loadWords(self) :
		cursor = self.database.cursor()
		cursor.execute("""SELECT id_word FROM words""")
		for id in cursor :
			words.append(self.constructWord(id))
		
	def isInDatabase(self, word) :
		if word is not None and word.kanjis != [] :
			cursor = self.database.cursor()
			wordsLike = []
			cursor.execute("""SELECT w_k.id_word FROM words_kanjis AS w_k INNER JOIN kanjis AS k ON w_k.id_kanji = k.id_kanji WHERE k.character like ?""", (word.kanjis[0].character,))
			for id in cursor :
				wordsLike.append(id)
			i = 1
			while wordsLike !=[] and i < (len(word.kanjis))
				cursor.execute("""SELECT w_k.id_word FROM words_kanjis AS w_k INNER JOIN kanjis AS k ON w_k.id_kanji = k.id_kanji WHERE k.character like ?""", (word.kanjis[i].character,))
				for id in cursor :
					wordsLike.append(id)
				i += 1
			# At that point the list wordsLike contains all the words longer than or equal to word whose word is a prefix
			for id in wordsLike :
				cursor.execute("""SELECT id_word FROM words_kanjis WHERE id_word = ? AND position = ?""", (id, len(word.kanjis)+1))
				result = cursor.fetchone()
				if result is not None :
					wordsLike.remove(result)
			return wordsLike != [] # If the wordsLike list is empty, then the word is not in the database, else it is
		return False
		
	def addWordToTable(self, word) : # /!\ does not add the kanjis to the related table, which must be done, preferably by KanjisManager : WordsManager calls its KanjisManager
		if not self.isInDatabase(word) :
			cursor.execute("""INSERT INTO words (kanas, studied_times)
							VALUES (?, ?)""", (word.kanas, word.studiedTimes,))
			cursor.execute("""SELECT id_word FROM words WHERE id_word = (SELECT max(id_word) FROM words)""")
			idWord = cursor.fetchone()[0]
			for m in word.meanings :
				cursor.execute("""SELECT id_meaning FROM meanings WHERE meaning like ?""", (m,))
				idMeaning = cursor.fetchone()[0]
				# checking if the meaning already exists in the database
				if idMeaning is None :
					# inserting the meaning in the table, then getting its id
					cursor.execute("""INSERT INTO meanings(meaning) VALUES (?)""", (meaning,))
					cursor.execute("""SELECT id_meaning FROM meanings WHERE meaning like ?""", (m,))
					idMeaning = cursor.fetchone()[0]
				# binding the word and its new meaning in the correspondence table
				cursor.execute("""INSERT INTO words_meanings(id_word, id_meaning) VALUES (?, ?)""", (idWord, idMeaning,))
			for k in word.kanjis :
				self.kanjisManager.addKanjiToTable(k) # /!\ the addKanjiToTable method must check some things before adding the kanji to the table
				cursor.execute("""INSERT INTO words_kanjis(id_word, id_kanji, position) VALUES (?, ?, ?)""", (idWord, self.kanjisManager.getId(k), k.position,)) # /!\ getId KanjisManager's method to implement ; testing the type of k might be necessary since the cast in python seems to be tricky
			self.database.commit()