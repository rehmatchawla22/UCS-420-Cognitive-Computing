import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Array:")
print(arr)

# a) Access 1st row, 2nd column
element1 = arr[0, 1]
print("1st row, 2nd column:", element1)

# b) Access 3rd row, 1st column
element2 = arr[2, 0]
print("3rd row, 1st column:", element2)