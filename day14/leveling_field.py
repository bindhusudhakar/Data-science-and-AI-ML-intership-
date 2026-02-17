import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Create dataset
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 50, 29],
    "Salary": [20000, 25000, 30000, 50000, 60000, 28000, 32000, 80000, 90000, 27000]
}

df = pd.DataFrame(data)

print(df)

scaler = StandardScaler()

df_standardized = pd.DataFrame(
    scaler.fit_transform(df),
    columns=df.columns
)

print(df_standardized)

minmax = MinMaxScaler()

df_normalized = pd.DataFrame(
    minmax.fit_transform(df),
    columns=df.columns
)

print(df_normalized)

# Original Salary
plt.figure()
plt.hist(df["Salary"])
plt.title("Original Salary Distribution")
plt.show()

# Standardized Salary
plt.figure()
plt.hist(df_standardized["Salary"])
plt.title("Standardized Salary Distribution")
plt.show()

# Normalized Salary
plt.figure()
plt.hist(df_normalized["Salary"])
plt.title("Normalized Salary Distribution")
plt.show()
