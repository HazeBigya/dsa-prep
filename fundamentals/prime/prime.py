import math

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def is_prime_math(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

num = 25
if is_prime(num):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
    
    
if is_prime_math(num):
    print(num, "is a prime number (using math method).")
else:
    print(num, "is not a prime number (using math method).")    