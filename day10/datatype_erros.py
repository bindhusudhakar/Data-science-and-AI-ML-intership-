import pandas as pd
data = {
    "Name" : ["Alice", "Bob", "Charlie"],
    "Marks" : ["85", "90", "88"]
}

df = pd.DataFrame(data)
print(df.dtypes)

df["Marks"] = df["Marks"].astype(int)
print(df.dtypes)
print(df["Marks"].mean())

data = {
    "Joining_Date": ["2024-01-10", "2023-12-05"]
}

df = pd.DataFrame(data)

print("Original Data Types:")
print(df.dtypes)
print("-" * 40)

df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("After Converting to Datetime:")
print(df.dtypes)
print("-" * 40)

print("Joining Year:")
print(df["Joining_Date"].dt.year)

data = {
    "Salary": ["50000", "60000", "Not Available"]
}

df = pd.DataFrame(data)

print("Before conversion:")
print(df.dtypes)

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")

print("\nAfter conversion:")
print(df.dtypes)
print(df)
