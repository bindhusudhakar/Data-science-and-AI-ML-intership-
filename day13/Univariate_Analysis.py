import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Price": [50000, 60000, 75000, 80000, 120000, 150000,
              200000, 300000, 450000, 1000000],   # skewed example
    "City": ["Bangalore", "Mumbai", "Delhi", "Bangalore",
             "Delhi", "Mumbai", "Mumbai", "Delhi",
             "Bangalore", "Mumbai"]
})
df["Price"] = np.log(df["Price"])
print(df)

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print("Skewness:", skewness)
print("Kurtosis:", kurtosis)

plt.figure()
sns.countplot(x="City", data=df)
plt.title("Count of Houses by City")
plt.show()
