import numpy as np

x = np.array([1, 2, 3, 4, 5, 1, 2, 1, 1, 1])

# Find unique values and their frequencies
values, counts = np.unique(x, return_counts=True)

# Find the index of the highest frequency
max_index = np.argmax(counts)

# Most frequent value
most_frequent = values[max_index]

# Find indices of the most frequent value
indices = np.where(x == most_frequent)[0]

print("Array:", x)
print("Most frequent value:", most_frequent)
print("Frequency:", counts[max_index])
print("Indices:", indices)