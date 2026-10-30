
import numpy as np

# Given data
X = np.array([
    [6, 70, 3],
    [5, 50, 6],
    [8, 80, 2],
    [4, 30, 8]
])

y = np.array([40, 65, 30, 85])

# a. Display shape and dimensions of X
print("Shape of X:", X.shape)
print("Dimensions of X:", X.ndim)

# b. Calculate transpose of X
X_transpose = X.T

print("\nTranspose of X:")
print(X_transpose)

# c. Calculate X.T @ X
product = X_transpose @ X

print("\nX.T @ X:")
print(product)

# d. Calculate matrix inverse
inverse = np.linalg.inv(product)

print("\nInverse of X.T @ X:")
print(inverse)

# e. Implement Ordinary Least Squares equation
beta = inverse @ X_transpose @ y

print("\nOLS coefficients:")
print(beta)

# f. Display the coefficients
print("\nSleep coefficient:", beta[0])
print("Activity coefficient:", beta[1])
print("Stress coefficient:", beta[2])

# g. Predict assistance score for a new user
new_user = np.array([5, 40, 7])

predicted_score = new_user @ beta

print("\nPredicted assistance score:", predicted_score)
