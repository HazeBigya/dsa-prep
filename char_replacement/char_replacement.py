def char_replacement(s, k):
    count = {}
    L = 0
    maxFreq = 0
    maxLen = 0
    
    for R in range(len(s)):
        count[s[R]] = count.get(s[R], 0) + 1
        maxFreq = max(maxFreq, count[s[R]])
        print("While Condition ", (R - L + 1) - maxFreq)
        while (R - L + 1) - maxFreq > k:
            count[s[L]] -= 1
            L += 1
        
        maxLen = max(maxLen, R - L + 1)
        before_window = s[:L]
        inside_window = s[L:R+1]
        after_window = s[R+1:]
        visual = f"{before_window}[{inside_window}]{after_window}"
        
        print(f"{visual:15} | L: {L}, R: {R} | maxFreq: {maxFreq} | whileCondition: {(R - L + 1) - maxFreq} | maxLen: {maxLen}")
        
    return maxLen

s = "AAABABABA"
k = 2
print("The Max length of the longest repeating charecter with replacement is: ", char_replacement(s, k))
            