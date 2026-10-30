#Q1(i)
roll_number = input("Enter your roll number: ")

digits = [int(digit) for digit in roll_number]

L = [digit * 10 for digit in digits]

print("Digits:", digits)
print("L:", L)

# Q1(ii)
L.append(100)
print("After append(100):", L)

# append() adds an element at the end of the list.

L.insert(2, 30)
print("After insert(2, 30):", L)

# insert() adds an element at the specified position.

#Q1(iii)
L.remove(100)
print("After remove(100):", L)

# remove() removes the specified value from the list.

removed = L.pop()
print("Element removed using pop():", removed)
print("After pop():", L)

# pop() removes and returns an element.
# By default, it removes the last element.

#Q1(iv)
L.sort()
print("Ascending order:", L)

L.sort(reverse=True)
print("Descending order:", L)

#Q1(v)
print("First three elements:", L[:3])
print("Last three elements:", L[-3:])

#Q1(vi)
average = sum(L) / len(L)

greater_than_average = [x for x in L if x > average]

print("Average:", average)
print("Elements greater than average:", greater_than_average)