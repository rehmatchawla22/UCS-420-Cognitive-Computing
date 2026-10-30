import numpy as np

y = np.array([1, 1, 1, 2, 3, 4, 2, 4, 3, 3])

# Find unique values and their frequencies
values, counts = np.unique(y, return_counts=True)

# Find index of maximum frequency
max_index = np.argmax(counts)

# Most frequent value
most_frequent = values[max_index]

# Find indices
indices = np.where(y == most_frequent)[0]

print("Array:", y)
print("Most frequent value:", most_frequent)
print("Frequency:", counts[max_index])
print("Indices:", indices)