def maximum_circular_subarray(nums):
    curr_max = curr_min = max_sum = min_sum = nums[0]
    total = sum(nums)

    for i in range(1, len(nums)):
        curr_max = max(nums[i], nums[i] + curr_max)
        curr_min = min(nums[i], nums[i] + curr_min)
        max_sum = max(max_sum, curr_max)
        min_sum = min(min_sum, curr_min)

    if max_sum < 0:
        return max_sum
    wrap = total - min_sum
    return max(wrap, max_sum)


print(maximum_circular_subarray([-2, 1, -3, 4, -1, 2, 1]))
