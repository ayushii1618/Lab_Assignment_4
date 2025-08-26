import numpy as np

# Create a 3x3 array of ones
original = np.ones((3, 3))
print("Original array:")
print(original)

# Create a 5x5 array of zeros
result = np.zeros((5, 5))

# Fill the center with ones
result[1:-1, 1:-1] = 1

print("\n1 on the border and 0 inside in the array\nOutput:\n")