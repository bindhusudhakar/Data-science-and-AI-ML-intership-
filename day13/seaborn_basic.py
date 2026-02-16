import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set(style="whitegrid")

data = { 
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F"]
}

df = pd.DataFrame(data)
print(df)

print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset shape (rows, columns):", df.shape)

print("\nDataset info:")
print(df.info())

