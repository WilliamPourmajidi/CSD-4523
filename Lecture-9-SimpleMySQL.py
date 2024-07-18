import mysql.connector


# Connection to MySQL
def connect_to_mysql():
    connection = mysql.connector.connect(
        host="localhost",  # Replace with your MySQL server host
        user="root",  # Replace with your MySQL username
        password="william"  # Replace with your MySQL password
    )
    return connection


def list_existing_databases(connection):
    """
    Function that takes a connection and shows all the databases in it
    :param connection:
    :return:
    """
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")  # This is a SQL command to list all databases
    databases = cursor.fetchall()
    print(databases)


# LISTING ALL THE DATABASES
# The following two lines are exactly doing the same thing as list_existing_databases(connect_to_mysql())
db_connection = connect_to_mysql()
list_existing_databases(db_connection)


def create_database(connection, db_name):
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    #     cursor.close()
    databases = cursor.fetchall()
    print(databases)


db_connection = connect_to_mysql()
create_database(db_connection, "william2024")


# Function to connect to a specific database
def connect_to_database(db_name):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="william",
        database=db_name
    )
    return connection


# connect to the database
db_connect = connect_to_database("william2024")


# Show the existing tables

def show_table(connection):
    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    tables = cursor.fetchall()
    print(f"Here are the tables  {tables}")


show_table(db_connect)


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

# Adding a table to a databsae
create_table(db_connect)


# Function to perform a Create operation
def insert_student(connection, name, age, major):
    cursor = connection.cursor()
    insert_query = "INSERT INTO students (name, age, major) VALUES (%s, %s, %s)"
    values = (name, age, major)
    cursor.execute(insert_query, values)
    connection.commit()
    cursor.close()
    print(f"Student '{name}' inserted successfully.")

# insert_student(db_connect,"Pranav",20,"FullStack Developer")
# insert_student(db_connect,"John",22,"FullStack Developer")
# insert_student(db_connect,"Elon",24,"FullStack Developer")
# insert_student(db_connect,"Bill",25,"FullStack Developer")



# Function to perform a Read operation
def read_students(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("Current students:")
    for row in rows:
        print(row)
    cursor.close()

read_students(db_connect)


# Function to perform an Update operation
def update_student_major(connection, student_id, new_major):
    cursor = connection.cursor()
    update_query = "UPDATE students SET major = %s WHERE id = %s"
    values = (new_major, student_id)
    cursor.execute(update_query, values)
    connection.commit()
    cursor.close()
    print(f"Student ID '{student_id}' updated successfully.")


update_student_major(db_connect, 36, "SpaceX and Tesla")




# Function to perform a Delete operation
def delete_student(connection, student_id):
    cursor = connection.cursor()
    delete_query = "DELETE FROM students WHERE id = %s"
    values = (student_id,)
    cursor.execute(delete_query, values)
    connection.commit()
    cursor.close()
    print(f"Student ID '{student_id}' deleted successfully.")

delete_student(db_connect, 37)