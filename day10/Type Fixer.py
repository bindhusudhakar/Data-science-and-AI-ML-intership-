import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Data Types BEFORE conversion:\n")
print(df.dtypes)

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nData Types AFTER conversion:\n")
print(df.dtypes)
