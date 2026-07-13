def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    raise ValueError("No two sum solution found.")

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of the two numbers that add up to the target:", result)  # Output: [0, 1]