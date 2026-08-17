def subarray_sum(nums, k):
    count = 0
    running = 0
    seen = {0: 1}

    for num in nums:
        running += num
        count += seen.get(running - k, 0)
        seen[running] = seen.get(running, 0) + 1

    return count


print(subarray_sum([1, 2, 3], 6))
print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([0, 0, 0], 0))
print(subarray_sum([3, -2, 5], 3))
