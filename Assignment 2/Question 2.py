#Q2
roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]

L = [digit * 10 for digit in digits]

scores = tuple(L[:8])

print("Scores:", scores)
# Q2(i)

highest = max(scores)
highest_index = scores.index(highest)

lowest = min(scores)
lowest_count = scores.count(lowest)

print("Highest score:", highest)
print("Index of highest score:", highest_index)
print("Lowest score:", lowest)
print("Lowest score appears:", lowest_count, "times")

# Q2(ii)

reversed_scores = scores[::-1]

print("Reversed tuple:", reversed_scores)

sorted_scores = tuple(sorted(scores))

print("Sorted tuple:", sorted_scores)

# Tuples are immutable, so their elements cannot be changed directly.

# Q2(iii)

score = int(input("Enter a score to search: "))

if score in scores:
    print("Score is present in the tuple.")
else:
    print("Score is not present in the tuple.")

# Q2(iv)

try:
    scores[0] = 100
except TypeError as e:
    print("Error:", e)

# A tuple is immutable, so its elements cannot be changed directly.
# A list is mutable, so its elements can be changed.

# Q2(v)

first, second, *remaining = scores

print("First score:", first)
print("Second score:", second)
print("Remaining scores:", remaining)



