import csv
import os

def create_folders_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            folder_name = row[0]  # Assuming the folder name is in the first column
            os.makedirs(folder_name, exist_ok=True)
            print(f"Created folder: {folder_name}")

# Replace 'path/to/your/csv/file.csv' with the actual path to your CSV file
csv_file_path = 'mynames.csv'
create_folders_from_csv(csv_file_path)