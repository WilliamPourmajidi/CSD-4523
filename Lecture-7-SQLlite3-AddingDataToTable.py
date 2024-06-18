import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO students (name, age, grade)
    VALUES ('William', 42, 'A')
''')

conn.commit()
conn.close()


