import csv

names = ["John", "Emma", "Michael", "Sophia", "William", "Olivia", "James", "Ava", "Benjamin", "Isabella"]

with open("C:/Users/heyrg/Desktop/PYTHON OS/mynames.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name"])
    writer.writerows([[name] for name in names])
    file.close()