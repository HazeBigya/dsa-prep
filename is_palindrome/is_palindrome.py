def is_palindrome(s):
    length = len(s)
    l = 0
    r = length - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True

str = "A man, a plan, a canal: Panama"
print("Is the string a palindrome?:", is_palindrome(str))