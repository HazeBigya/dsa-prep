def febonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    febonacci = [0, 1]
    
    for i in range(2, n, 1):
        febonacci.append(febonacci[i-1] + febonacci[i-2])
        
    return febonacci

def febonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    prev1 = 0
    prev2 = 1
    curr = 0
    for i in range(2, n + 1, 1):
        curr = prev1 + prev2
        prev1= prev2
        prev2 = curr
    return curr

num = 10
print("The Fibonacci series up to", num, "is:", febonacci_series(num))
print("The", num, "th Fibonacci number is:", febonacci(num))