def palindrome_number(n):
    reversed = 0
    original = n
    
    if n == 0: return True
    elif n < 0: return False
    else:
        while n > 0:
            num = n % 10
            reversed = reversed * 10 + num
            n = n // 10
        if reversed == original: return True
        else: return False
        
n = 1234321
print("Is the number a palindrome: ", palindrome_number(n))

    