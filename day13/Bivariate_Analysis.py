import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "SquareFootage": [800, 1200, 1500, 2000, 2200, 2500, 3000, 1800, 1600, 2800],
    "Price": [40, 60, 75, 120, 135, 150, 200, 110, 90, 180],
    "City": ["A", "B", "A", "C", "B", "C", "A", "B", "A", "C"]
}

df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(7,5))
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="City", y="Price", data=df)
plt.title("Price Distribution by City")
plt.show()
