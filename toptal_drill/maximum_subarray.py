def maximum_subarray(nums):
    best = current = nums[0]
    for i in range(1, len(nums)):
        current = max(nums[i], current + nums[i])
        best = max(current, best)
    return best


print("The Max subarray sum is: ", maximum_subarray([-2, 1, -3, 4, -1, 2, 1]))
print("The Max subarray sum is: ", maximum_subarray([-3, -1, -2]))
print("The Max subarray sum is: ", maximum_subarray([5]))
print("The Max subarray sum is: ", maximum_subarray([-7]))
print("The Max subarray sum is: ", maximum_subarray([5, -3, 5]))
