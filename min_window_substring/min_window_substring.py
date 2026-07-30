from collections import Counter

def min_window_substring(s, t):
    if not t or not s:
        return ""
    
    need = Counter(t)
    need_count = len(need)
    window= {}
    have = 0
    res = ""
    res_length = float('inf')
    L = 0
    
    for R in range(len(s)):
        c = s[R]
        window[c] = window.get(c, 0) + 1
        if c in need and window.get(c) == need.get(c):
            have += 1
        while have == need_count:
            if(R - L +1) < res_length:
                res_length = R - L + 1
                res = s[L: R + 1]
            left_c = s[L]
            window[left_c] -= 1
            if left_c in need and window[left_c] < need[left_c]:
                have -= 1
            L += 1
    return res
    
    print(window)

s = "ADOBECODEBANC"
t = "ABC"
print("The shortest substring is: ", min_window_substring(s, t));