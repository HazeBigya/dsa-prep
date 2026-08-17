def largest_rectangle_area(heights):
    heights.append(0)
    stack = []
    max_area = 0

    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            if stack:
                left_wall = stack[-1]
            else:
                left_wall = -1
            width = i - left_wall - 1
            max_area = max(max_area, h * width)
        stack.append(i)

    return max_area


print(largest_rectangle_area([2, 1, 5, 6, 2, 3]))
