def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10;
        n = n // 10
    return sum

def count_of_digits(n):
    count = 0
    if n == 0: return 1;
    while n > 0:
        count += 1
        n = n // 10
    return count

n = 5451
print("The sum of digits is: ",sum_of_digits(n))
print("The count of digits is: ",count_of_digits(n))