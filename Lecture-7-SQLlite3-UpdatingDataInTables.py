import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE python_students
    SET grade = 'C'
    WHERE name = 'William'
''')



conn.commit()
conn.close()


