def factorial(n):
    if n == 0: return 1
    return n * factorial(n -1)

def factorial_iteration(n):
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product

n = 5
print('The factorial of', n , 'is:', factorial(n))
print('The factorial of', n , 'with itegration is:', factorial_iteration(n))