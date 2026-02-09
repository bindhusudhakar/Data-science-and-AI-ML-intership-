import csv

with open("day6/data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])


with open("day6/data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)