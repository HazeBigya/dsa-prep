def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        L = i + 1
        R = n - 1
        target = -nums[i]

        while L < R:
            curr_sum = nums[L] + nums[R]
            if curr_sum == target:
                result.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
            elif curr_sum < target:
                L += 1
            else:
                R -= 1
    return result


nums = [-1, 0, 1, 2, -1, -4]
print("The Three sum of the array is: ", three_sum(nums))
