import numpy as np
from sklearn.linear_model import LinearRegression

# Dataset
X = np.array([
    [8,1],
    [8,3],
    [12,1],
    [12,4],
    [16,2]
])

y = np.array([10,13,18,22.5,28])

# Model
model = LinearRegression()
model.fit(X, y)

# Prediction
predicted_price = model.predict([[10,2]])

print("Predicted Price:", predicted_price)