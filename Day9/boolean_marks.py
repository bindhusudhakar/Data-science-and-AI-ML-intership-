import pandas as pd 

marks = pd.Series([78, 85, 92, 60, 80], ['A', 'B', 'C', 'D', 'E'])

print(marks)

marks = marks >= 80
print(marks)

filtered_marks = marks[marks]
print(filtered_marks)

print(marks[marks >= 80])

print(marks[(marks >= 80)& (marks < 80)])

marks[marks < 70] =70
print(marks)