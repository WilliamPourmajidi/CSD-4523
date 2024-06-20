# Import the logging module
import logging

# Set up the basic configuration for logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to load a file
def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            logging.info(f"Successfully loaded the file: {file_path}")
            return data
    except FileNotFoundError:
        logging.critical(f"The file {file_path} does not exist.")
        return None

# Attempt to load a file
file_path = 'my_file.txt'
file_data = load_file(file_path)

if file_data is not None:
    print(f"here is the content of the {file_path}\n {file_data}")
else:
    print(f"Failed to load the file: {file_path}")
