import csv

data = [
    ["Name", "Score"],
    ["Ramesh", 85],
    ["Anitha", 90]
]

with open("day6/results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)