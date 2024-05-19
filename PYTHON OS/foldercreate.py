import os

path = './'

# Create 10 folders
for i in range(1, 11):
    folder_name = f'folder{i}'
    folder_path = os.path.join(path, folder_name)
    os.makedirs(folder_path)
    print(f'Folder {folder_name} created successfully.')