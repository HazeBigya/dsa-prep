def longest_substring(s):
    seen = set()
    L = 0
    maxLen = 0
    for R in range (len(s)):
        while s[R] in seen:
            seen.remove(s[L])
            L += 1
        seen.add(s[R])
        maxLen = max(maxLen, R - L + 1)
    return maxLen

s = "abcabcbb"
print("The longest substring length is :", longest_substring(s))

