import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE python_students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade TEXT
    )
''')

conn.commit()
conn.close()