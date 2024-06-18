
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    DELETE FROM students
    WHERE name = 'William'
''')

conn.commit()
conn.close()


