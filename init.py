import sqlite3

db = sqlite3.connect('database.db')

cur = db.cursor()

cur.execute("CREATE TABLE tble (a,b)")

db.commit()