import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current Working Directory: {cwd}")
#
# # List all files and directories in the current directory
items = os.listdir(cwd)
print(f"Items in {cwd}: {items}")
#
# # Create a new directory
new_dir = os.path.join(cwd, 'new_directory')
os.mkdir(new_dir)
print(f"Directory 'new_directory' created")
#
# # Rename the new directory
renamed_dir = os.path.join(cwd, 'renamed_directory')
os.rename(new_dir, renamed_dir)
print(f"Directory renamed to 'renamed_directory'")

# Remove the renamed directory
os.rmdir(renamed_dir)
print(f"Directory 'renamed_directory' removed")



