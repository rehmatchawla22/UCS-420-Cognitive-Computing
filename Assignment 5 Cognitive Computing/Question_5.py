import numpy as np

# Create 2-D array with 3 rows and 4 columns
ucs420_Rehmat = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 15, 20, 35]
])

print("Original Array:")
print(ucs420_Rehmat)

# Mean
print("\nMean:", np.mean(ucs420_Rehmat))

# Median
print("Median:", np.median(ucs420_Rehmat))

# Maximum
print("Maximum:", np.max(ucs420_Rehmat))

# Minimum
print("Minimum:", np.min(ucs420_Rehmat))

# Unique elements
print("Unique elements:", np.unique(ucs420_Rehmat))

# Reshape to 4 rows and 3 columns
reshaped_ucs420_Rehmat = ucs420_Rehmat.reshape(4, 3)

print("\nReshaped Array (4 x 3):")
print(reshaped_ucs420_Rehmat)

# Resize to 2 rows and 3 columns
resized_ucs420_Rehmat = np.resize(ucs420_Rehmat, (2, 3))

print("\nResized Array (2 x 3):")
print(resized_ucs420_Rehmat)