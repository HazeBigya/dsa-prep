def maximum_circular_subarray(nums):
    curr_max = curr_min = max_sum = min_sum = nums[0]
    total = sum(nums)
    for i in range(1, len(nums)):
        curr_max = max(nums[i], curr_max + nums[i])
        curr_min = min(nums[i], curr_min + nums[i])
        max_sum = max(curr_max, max_sum)
        min_sum = min(curr_min, min_sum)

    if max_sum < 0:
        return max_sum
    wrap = total - min_sum
    return max(wrap, max_sum)


print(
    "The max sum in a circular subarray is: ",
    maximum_circular_subarray([1, 2, -3, -4, 5, -6, 7, 8, -9]),
)
print(
    "The max sum in a circular subarray is: ",
    maximum_circular_subarray([-2, 1, -3, 4, -1, 2, 1]),
)
print("The max sum in a circular subarray is: ", maximum_circular_subarray([5, -3, 5]))
print(
    "The max sum in a circular subarray is: ", maximum_circular_subarray([-3, -2, -5])
)
print("The max sum in a circular subarray is: ", maximum_circular_subarray([3, 2, 5]))
