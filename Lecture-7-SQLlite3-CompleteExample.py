import sqlite3

# Step 1: Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example.db')

# Step 2: Create a cursor object
cursor = conn.cursor()

# Step 3: Create a new table if it doesn't exist
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS fullstack_students (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         age INTEGER NOT NULL,
#         grade TEXT NOT NULL
#     )
# ''')

#Let's list all the tables in our database

# cursor.execute('''
# SELECT name FROM sqlite_master WHERE type='table'
# ''')
# print(cursor.fetchall())
#


# Step 4: Insert records into the table using a loop and placeholders
# students_data = [
#     ("Alice Johnson", 20, 'A'),
#     ("Bob Smith", 22, 'B'),
#     ("Charlie Brown", 21, 'C'),
#     ("William P", 42, 'A')
# ]
#
#
# for student in students_data:
#     cursor.execute('''
#         INSERT INTO fullstack_students (name, age, grade)
#         VALUES (?, ?, ?)
#     ''', student)
#
#
#
# # Step 5: Commit the transaction
# conn.commit()

# Step 6: Fetch and display the records
cursor.execute('SELECT * FROM fullstack_students')
rows = cursor.fetchall()
print(type(rows))
print("Students Data:")
for row in rows:
    print(row)

# # Step 7: Close the connection
conn.close()
