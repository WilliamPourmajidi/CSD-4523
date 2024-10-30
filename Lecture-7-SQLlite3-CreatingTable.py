import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE python_students (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         grade TEXT
#     )
# ''')
cursor.execute('''
    SELECT * FROM python_students''')

rows = cursor.fetchall()
for row in rows:
    print(row)

print("database table is created successfully!")

conn.commit()
conn.close()