import numpy as np

# Create an array named Rehmat with 25 evenly spaced numbers from 10 to 100
Rehmat = np.linspace(10, 100, 25)

print("Original Array:")
print(Rehmat)

# Number of dimensions
print("\nDimensions:", Rehmat.ndim)

# Shape of the array
print("Shape:", Rehmat.shape)

# Total number of elements
print("Total elements:", Rehmat.size)

# Data type
print("Data type:", Rehmat.dtype)

# Total number of bytes
print("Total bytes:", Rehmat.nbytes)

# Transpose using reshape()
transpose_reshape = Rehmat.reshape(1, 25)

print("\nTranspose using reshape():")
print(transpose_reshape)

# Transpose using T attribute
transpose_T = Rehmat.T

print("\nTranspose using T attribute:")
print(transpose_T)