import sqlite3


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
        FOREIGN KEY(structure) REFERENCES structure(structure_id)
    )
''')
db.commit()


cursor.execute("DROP TABLE info")
cursor.execute("DROP TABLE structure")
db.commit()

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