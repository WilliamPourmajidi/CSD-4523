import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE students
    SET grade = 'B'
    WHERE name = 'William'
''')

conn.commit()
conn.close()


