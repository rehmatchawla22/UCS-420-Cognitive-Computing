# Q5 

my_dict = {
    "name": "Rehmat",
    "roll_no": "1024170095",
    "branch": "CSE",
    "age": 20,
    "city": "Amritsar"
}

print("Original dictionary:")
print(my_dict)


# Q5(i) 

location = my_dict.pop("city")
my_dict["location"] = location

print("\nAfter renaming city to location:")
print(my_dict)


# Q5(ii)

my_dict["cgpa"] = 8.5

print("\nAfter adding CGPA:")
print(my_dict)


# Q5(iii) 

my_dict["age"] += 1

print("\nAfter increasing age by 1:")
print(my_dict)


# Q5(iv) 

dict_pop = my_dict.copy()

removed_branch = dict_pop.pop("branch")

print("\nAfter deleting branch using pop():")
print(dict_pop)


dict_del = my_dict.copy()

del dict_del["branch"]

print("\nAfter deleting branch using del:")
print(dict_del)

# pop() removes the key and returns its value,
# while del removes the key but does not return its value.


# Q5(v) 

print("\nKey-value pairs:")

for key, value in my_dict.items():
    print(key, "→", value)


# Q5(vi) 

print("\nChecking for email:")

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email not found.")


# Q5(vii)

friend_dict = {
    "name": "Rahul",
    "roll_no": "1234567890",
    "branch": "ECE",
    "age": 21,
    "city": "Amritsar"
}

print("\nFriend dictionary:")
print(friend_dict)


# Merge dictionaries

merged_dict = {**my_dict, **friend_dict}

print("\nMerged dictionary:")
print(merged_dict)

# When the same key exists in both dictionaries,
# the value from the dictionary written later wins.
# Here, friend_dict values overwrite my_dict values.


# Q5(viii)

string_dict = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}

print("\nDictionary containing only string values:")
print(string_dict)