# Importing the necessary libraries
import mysql.connector

# Function to connect to MySQL database
def connect_to_mysql():
    # Establishing a connection to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL server host
        user="your_username",  # Replace with your MySQL username
        password="your_password"  # Replace with your MySQL password
    )
    return connection

# Function to list current databases
def list_databases(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    databases = cursor.fetchall()
    print("Current databases:")
    for db in databases:
        print(db[0])
    cursor.close()

# Function to create a new database
def create_database(connection, db_name):
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    cursor.close()
    print(f"Database '{db_name}' created successfully.")

# Function to connect to a specific database
def connect_to_database(db_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database=db_name
    )
    return connection

# Function to create a new table
def create_table(connection):
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT NOT NULL,
        major VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    cursor.close()
    print("Table 'students' created successfully.")

# Function to perform a Create operation
def insert_student(connection, name, age, major):
    cursor = connection.cursor()
    insert_query = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
    values = (name, age, major)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    print(f"Student '{name}' inserted successfully.")

# Function to perform a Read operation
def read_students(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("Current students:")
    for row in rows:
        print(row)
    cursor.close()

# Function to perform an Update operation
def update_student_major(connection, student_id, new_major):
    cursor = connection.cursor()
    update_query = "UPDATE students SET major = %s WHERE id = %s"
    values = (new_major, student_id)
    cursor.execute(update_query, values)
    connection.commit()
    cursor.close()
    print(f"Student ID '{student_id}' updated successfully.")

# Function to perform a Delete operation
def delete_student(connection, student_id):
    cursor = connection.cursor()
    delete_query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(delete_query, values)
    connection.commit()
    cursor.close()
    print(f"Student ID '{student_id}' deleted successfully.")

# Main function to demonstrate the complete workflow
def main():
    # Connect to MySQL server
    connection = connect_to_mysql()

    # List current databases
    list_databases(connection)

    # Create a new database
    db_name = "college"
    create_database(connection, db_name)

    # Connect to the new database
    connection.close()
    connection = connect_to_database(db_name)

    # Create a new table in the database
    create_table(connection)

    # Insert a new student (Create operation)
    insert_student(connection, "John Doe", 20, "Computer Science")

    # Read and display current students (Read operation)
    read_students(connection)

    # Update a student's major (Update operation)
    update_student_major(connection, 1, "Software Engineering")

    # Read and display updated students
    read_students(connection)

    # Delete a student (Delete operation)
    delete_student(connection, 1)

    # Read and display students after deletion
    read_students(connection)

    # Close the database connection
    connection.close()

if __name__ == "__main__":
    main()
