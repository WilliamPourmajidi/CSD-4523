import sqlite3

# Connect to a database (or create one if it doesn't exist)
conn = sqlite3.connect('example-wed.db')

# Create a cursor object
cursor = conn.cursor()
