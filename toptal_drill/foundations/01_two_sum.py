def two_sums(nums, target):
    seen = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return [seen[diff], i]
        seen[nums[i]] = i


nums = [2, 7, 9, 11, 15, 21]
target = 20

print(f"The index's that has the sum of target {target} are : {two_sums(nums, target)}")
