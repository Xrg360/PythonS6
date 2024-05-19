import os

path = './'

# Delete 10 folders
for i in range(1, 11):
    folder_name = f'folder{i}'
    folder_path = os.path.join(path, folder_name)
    if os.path.exists(folder_path):
        os.rmdir(folder_path)
        print(f'Folder {folder_name} deleted successfully.')
    else:
        print(f'Folder {folder_name} does not exist.')