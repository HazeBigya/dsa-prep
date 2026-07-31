def largest_rectangle(heights):
    max_area = 0
    stack = []
    n = len(heights)
    
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * width)
        stack.append(i)
        
    while stack:
        h = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * width)
        
    return max_area

heights = [2, 1, 5, 6, 2, 3]
print("The max area of the rectangle is: ", largest_rectangle(heights))