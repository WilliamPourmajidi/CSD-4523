import sys


# Get the version of Python interpreter
python_version = sys.version
print(f"Python Version: {python_version}")

# Get the list of command line arguments
arguments = sys.argv
print(f"Command Line Arguments: {arguments}")

# Exit the program with a status code
print("Exiting the program")
sys.exit(0)
