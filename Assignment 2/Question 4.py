# Q4 

roll_number = "1024170095"

digits = [int(digit) for digit in roll_number]

# Use the first 8 digits
first_eight = digits[:8]

# Create sets
A = {digit for digit in first_eight if digit > 7}

B = {digit for digit in first_eight if digit < 9}

print("First 8 digits:", first_eight)
print("A:", A)
print("B:", B)


# Q4(vi) 

union = A.union(B)

print("\nUnion of A and B:", union)


# Q4(vii) 

intersection = A.intersection(B)

print("Intersection of A and B:", intersection)


# Q4(viii)
A_minus_B = A.difference(B)
B_minus_A = B.difference(A)

print("A - B:", A_minus_B)
print("B - A:", B_minus_A)

# A-B contains elements only in A, while B-A contains
# elements only in B, so they can be different.


# Q4(ix) 

symmetric_difference = A.symmetric_difference(B)

print("Symmetric difference:", symmetric_difference)


# Q4(x)

print("Is A a subset of B?", A.issubset(B))
print("Is B a subset of A?", B.issubset(A))

print("Is A a superset of B?", A.issuperset(B))
print("Is B a superset of A?", B.issuperset(A))


# Q4(xi) 

X = int(input("\nEnter a value X: "))

if X in A:
    A.discard(X)
    print(X, "was present and has been removed.")
else:
    A.discard(X)
    print(X, "was not present.")

print("Updated A:", A)

# discard() is safer than remove() because it does not raise
# an error when the element is not present.