import numpy as np

data = np.array([[10, 20, 30], [40, 50, 60]])
print(np.mean(data))
print(np.mean(data,axis=0))

print("Mean (axis=1):", np.mean(data, axis=1))
print("Median (axis=1):", np.median(data, axis=1))
print("Std Dev (axis=1):", np.std(data, axis=1))


import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

result = A @ B   # or np.dot(A, B)
print(result)