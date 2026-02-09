import csv

with open("day6/student.csv" , "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
