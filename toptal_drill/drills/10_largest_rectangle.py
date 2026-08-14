def largestRectangleArea(heights):
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


if __name__ == "__main__":
    tests = [
        # (heights, expected)
        ([2, 1, 5, 6, 2, 3], 10),  # LeetCode sample -> bars 5,6 capped at 5, width 2
        ([2, 4], 4),  # tall single bar beats the pair (2x2)
        ([1], 1),  # single bar
        ([2, 2, 2], 6),  # all equal -> full width
        ([5, 4, 3, 2, 1], 9),  # strictly decreasing -> pops every step
        ([1, 2, 3, 4, 5], 9),  # strictly increasing -> nothing pops till sentinel
        ([0], 0),  # zero height
        ([1, 1], 2),  # equal heights, width 2
        ([6, 7, 5, 2, 4, 5, 9, 3], 16),  # two separate candidate regions
    ]

    failed = 0
    for heights, expected in tests:
        got = largestRectangleArea(list(heights))  # copy: the fn appends a sentinel
        ok = got == expected
        failed += not ok
        print(
            f"{'PASS' if ok else 'FAIL'}  heights={heights} expected={expected} got={got}"
        )

    print()
    print("ALL PASS" if failed == 0 else f"{failed} FAILED")
