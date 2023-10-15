import sqlite3
from datasets import *

db = sqlite3.connect('db.sqlite3')

cursor = db.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS structure(
        id INTEGER PRIMARY KEY,
        name TEXT
    )
''')
db.commit()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS info(
        id INTEGER PRIMARY KEY,
        region TEXT,
        year INTEGER,
        presenze INTEGER,
        arrivi INTEGER,
        structure INTEGER,
        FOREIGN KEY(structure) REFERENCES structure(id)
    )
''')
db.commit()

df.to_sql('info', db, if_exists='replace', index=False)
db.commit()