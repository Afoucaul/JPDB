#-*- coding: utf-8 -*-

# Author : Armand FOUCAULT

from sqlite3 import *

DB = connect('kanjis.db')

cursor = DB.cursor()


# Dropping the tables #################################################

cursor.execute("""
DROP TABLE IF EXISTS words;
""")	

cursor.execute("""
DROP TABLE IF EXISTS kanjis;
""")
	
cursor.execute("""
DROP TABLE IF EXISTS words_kanjis;
""")
	
cursor.execute("""
DROP TABLE IF EXISTS meanings;
""")		
	
cursor.execute("""
DROP TABLE IF EXISTS words_meanings;
""")	
	
cursor.execute("""
DROP TABLE IF EXISTS kanjis_meanings;
""")	

DB.commit()

# Creating the tables #################################################

cursor.execute("""
CREATE TABLE words(
	id_word INTEGER NOT NULL PRIMARY KEY,
	kanas VARCHAR(200),
	studied_times INTEGER
);
""")

cursor.execute("""
CREATE TABLE kanjis(
	id_kanji INTEGER NOT NULL PRIMARY KEY,
	character VARCHAR(50),
	strokes INTEGER
);
""")

cursor.execute("""
CREATE TABLE words_kanjis(
	id_word INTEGER NOT NULL REFERENCES words(id_word),
	id_kanji INTEGER NOT NULL REFERENCES kanjis(id_kanji),
	position INTEGER NOT NULL,
	PRIMARY KEY (id_word, position)
);
""")

cursor.execute("""
CREATE TABLE meanings(
	id_meaning INTEGER NOT NULL PRIMARY KEY,
	meaning VARCHAR(100)
);
""")

cursor.execute("""
CREATE TABLE words_meanings(
	id_word INTEGER NOT NULL REFERENCES words(id_word),
	id_meaning INTEGER NOT NULL REFERENCES meanings(id_meaning),
	PRIMARY KEY (id_word, id_meaning)
);
""")

cursor.execute("""
CREATE TABLE kanjis_meanings(
	id_kanji INTEGER NOT NULL REFERENCES kanjis(id_kanji),
	id_meaning INTEGER NOT NULL REFERENCES meanings(id_meaning),
	PRIMARY KEY (id_word, id_meaning)
);
""")

DB.commit()

DB.close()