
import numpy as np

# a. Create the original array
original = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", original)

# b. Create a slice from index 1 to 4
subset = original[1:5]
print("Subset:", subset)

# c. Modify the first element of subset
subset[0] = 999

print("Original after modifying subset:", original)
print("Modified subset:", subset)

# d. Create another slice using copy()
copied_array = original[1:5].copy()

copied_array[0] = 500

print("Original after modifying copied array:", original)
print("Copied array:", copied_array)

# e. Create a 3x4 matrix using arange()
matrix = np.arange(1, 13).reshape(3, 4)

print("\n3x4 Matrix:")
print(matrix)

# f. Extract rows, columns, and elements

# First row
print("First row:", matrix[0, :])

# Last row
print("Last row:", matrix[-1, :])

# Second column
print("Second column:", matrix[:, 1])

# Rows 1-2 and columns 2-3
print("Selected elements:")
print(matrix[1:3, 2:4])

# g. Flatten using flatten() and ravel()
flat_array = matrix.flatten()
ravel_array = matrix.ravel()

print("\nFlatten array:", flat_array)
print("Ravel array:", ravel_array)

# h. Modify an element in ravel()
ravel_array[0] = 100

print("Matrix after modifying ravel:")
print(matrix)

# i. Modify an element in flatten()
flat_array[1] = 200

print("Matrix after modifying flatten:")
print(matrix)

# j. Display matrix properties
print("\nShape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data type:", matrix.dtype)
