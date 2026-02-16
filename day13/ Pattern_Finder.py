import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "SquareFootage": [800, 1200, 1500, 2000, 2200, 2500, 3000, 1800, 1600, 2800],
    "Price": [40, 60, 75, 120, 135, 150, 200, 110, 90, 180],
    "Bedrooms": [2, 3, 3, 4, 4, 5, 5, 3, 3, 5],
    "City_Code": [1, 2, 1, 3, 2, 3, 1, 2, 1, 3]
}

df = pd.DataFrame(data)
print(df)

correlation_matrix = df.corr()
print(correlation_matrix)

plt.figure(figsize=(6,5))
sns.heatmap(correlation_matrix, annot=True, cmap="seismic")
plt.title("Correlation Matrix Heatmap")
plt.show()
plt.figure(figsize=(6,4))
sns.boxplot(y="Price", data=df)
plt.title("Boxplot of Price")
plt.show()
