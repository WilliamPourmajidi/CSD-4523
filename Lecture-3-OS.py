import os

# List the current working directory - the one that our python code is located in!
current_working_directory = os.getcwd()
print(f"Here is the current working directory: {current_working_directory}")

# List all files and directories (items) in a directory
items = os.listdir(current_working_directory)
print(f"Here are the current items in {current_working_directory}: {items}")

# Creating a new folder
path_to_new_folder = os.path.join(current_working_directory, 'my_new_dir')
print(path_to_new_folder)
os.mkdir(path_to_new_folder)
print(f"Directory {path_to_new_folder} created")


# Rename the new directory
renamed_dir = os.path.join(current_working_directory, 'renamed_directory')
os.rename(path_to_new_folder, renamed_dir)
print(f"Directory renamed to 'renamed_directory'")


# Remove the renamed directory
os.rmdir(renamed_dir)
print(f"Directory 'renamed_directory' removed")
