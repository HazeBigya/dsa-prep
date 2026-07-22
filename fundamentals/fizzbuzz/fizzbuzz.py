def fizz_buzz(n):
    arr = []
    for i in range (1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            arr.append("FizzBuzz")
        elif (i % 3 == 0):
            arr.append("Fizz")
        elif (i % 5 == 0):
            arr.append("Buzz")
        else:
            arr.append(i)
            
    return arr;

n = 15
print(fizz_buzz(n))