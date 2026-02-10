import numpy as np

data = np.arange(24)
print("Original 1D array:")
print(data)

reshaped_data = data.reshape(4, 3, 2)

print("\nReshaped array (4, 3, 2):")
print(reshaped_data)

transposed_data = reshaped_data.transpose(0, 2, 1)

print("\nFinal Shape:")
print(transposed_data.shape)

print("\nFinal Transposed Array:")
print(transposed_data)
