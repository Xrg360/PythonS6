#write a python program to calculate teh number of rows in a csv file
import csv
filename = 'data.csv'
rows = 0
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        rows += 1
print(f"The number of rows in the CSV file '{filename}' is: {rows}")
