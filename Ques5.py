import numpy as np

# Define the arrays
array1 = np.array([0, 10, 20, 40, 60])
array2 = np.array([0, 40])

print("Array1:", array1)
print("Array2:", array2)
print("Compare each element of array1 and array2")

# Use np.isin instead of np.in1d
result = np.isin(array1, array2)

print(result)

