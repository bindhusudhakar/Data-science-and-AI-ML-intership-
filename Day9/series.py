import pandas as pd

df = pd.read_excel("Student_Performance_Dataset (1).xlsx")
print("Full DataFrame:\n")
print(df)

s = pd.Series([10, 20, 30, 40])
print("\nSimple Series:\n")
print(s)

marks = pd.Series([85, 90, 78], index=["Maths", "Science", "English"])
print("\nMarks Series:\n")
print(marks)

print(marks[0])

print(marks["Science"])

print(marks[["Maths", "English"]])

print(marks[0:2])

print(marks[["Maths", "Science"]])

print(marks + 5)

print(marks[marks > 80])