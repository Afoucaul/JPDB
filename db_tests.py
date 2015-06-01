from sqlite3 import *

db = connect("C:/Users/Armand/Documents/Programmation/Python/JPDB/kanjis.db")

c = db.cursor()

c.execute("INSERT INTO words(kanas, studied_times) VALUES (