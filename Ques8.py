import numpy as np

# Take input for the matrix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter the elements row-wise (separated by space):")
matrix = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert to numpy array
A = np.array(matrix)

print("\nInput Matrix:")
print(A)

# Calculate rank, trace, determinant
rank = np.linalg.matrix_rank(A)
trace = np.trace(A)

# Determinant is only defined for square matrices
if rows == cols:
    determinant = np.linalg.det(A)
else:
    determinant = "Not defined (matrix is not square)"

print("\nMatrix Properties:")
print("Rank:", rank)
print("Trace:", trace)
print("Determinant:", determinant)
