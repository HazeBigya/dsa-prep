from collections import Counter

def isAnagram(s: str, t:str) -> bool:
    if len(s) != len(t):
        return False
    count_s = {}
    count_t = {}
    for char in s:
         count_s[char] = count_s.get(char, 0) + 1
    for char in t:
        count_t[char] = count_t.get(char, 0) + 1
    return count_s == count_t   

def isAnagramUsingCounter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

s = "anagram"
t = "nagaram"
print("The strings are anagrams:", isAnagram(s, t))  # Output: True
print("The strings are anagrams (using Counter):", isAnagramUsingCounter(s, t))  # Output: True