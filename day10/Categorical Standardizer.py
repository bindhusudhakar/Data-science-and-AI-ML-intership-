import pandas as pd

df = pd.read_csv("customer_orders.csv")

df.columns = df.columns.str.strip()

print("Columns in dataset:")
print(df.columns)

print("\nUnique values BEFORE cleaning:")
print(df["customer_id"].unique())   

df["customer_id"] = df["customer_id"].str.strip().str.title()

print("\nUnique values AFTER cleaning:")
print(df["customer_id"].unique())

