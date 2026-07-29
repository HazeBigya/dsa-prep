def daily_temperatures(temp):
    n = len(temp)
    answer = [0] * n
    stack = []
    
    for i in range(0, n):
        while stack and temp[i] > temp[stack[-1]]:
            top = stack.pop()
            answer[top] = i - top
        stack.append(i)
    
    return answer
        
temp = [73,74,75,71,69,72,76,73]
print("The days before a warmer temperature is: ", daily_temperatures(temp))