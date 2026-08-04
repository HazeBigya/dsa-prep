def three_sum(nums):
    nums.sort()
    n = len(nums)
    res = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        L = i + 1
        R = n - 1
        target = -nums[i]

        while L < R:
            curr_sum = nums[L] + nums[R]
            if curr_sum == target:
                res.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L] == nums[L - 1]:
                    L += 1
            elif curr_sum < target:
                L += 1
            else:
                R -= 1

    return res


nums = [-1, 0, 1, 2, -1, -4]
print("The Three sum of the array is: ", three_sum(nums))
