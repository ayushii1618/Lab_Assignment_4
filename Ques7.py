import numpy as np

# Define the arrays
array1 = np.array([10, 20, 30])
array2 = np.array([40, 50, 60])

print("Array1:", array1)
print("Array2:", array2)

# Stack arrays column-wise
result = np.column_stack((array1, array2))

print("Stacked Arrays column-wise:")
print(result)
