# Import the logging module
import logging

# Set up the basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to load a file
def load_file(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            logging.info(f"Successfully loaded the file: {file_name}")
            return data
    except FileNotFoundError:
        logging.critical(f"The file {file_name} does not exist.")
        return None

# Attempt to load a file
file_name = 'my_file.txt'
file_data = load_file(file_name)
print (f"This is the content of the file: \n {file_data}")

