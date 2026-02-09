import csv

with open("day6/data.csv" , "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
