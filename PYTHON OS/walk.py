import os

# Define the root directory to start walking from
root_directory = '/path/to/your/directory'

# Walk through the directory tree
for current_dir, subdirs, files in os.walk(root_directory):
    print("Current Directory:", current_dir)
    print("Subdirectories:", subdirs)
    print("Files:", files)
    print()
