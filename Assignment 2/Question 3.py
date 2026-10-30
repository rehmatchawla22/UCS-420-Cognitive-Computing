# Q3

import random
from collections import Counter


# Set random seed using roll number
roll_number = 1024170095

random.seed(roll_number)


# Q3(i)


random_numbers = [random.randint(0, 100) for _ in range(100)]

print("Random numbers:")
print(random_numbers)


# Q3(ii)


odd_numbers = [x for x in random_numbers if x % 2 != 0]

print("\nOdd numbers:")
print(odd_numbers)

print("Number of odd numbers:", len(odd_numbers))


# Q3(iii)


even_numbers = [x for x in random_numbers if x % 2 == 0]

print("\nEven numbers:")
print(even_numbers)

print("Number of even numbers:", len(even_numbers))


# Q3(iv)


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


prime_numbers = [x for x in random_numbers if is_prime(x)]

print("\nPrime numbers:")
print(prime_numbers)

print("Number of prime numbers:", len(prime_numbers))


# Q3(v)


frequency = Counter(random_numbers)

number, count = frequency.most_common(1)[0]

print("\nMost frequently occurring number:", number)
print("It occurs", count, "times.")