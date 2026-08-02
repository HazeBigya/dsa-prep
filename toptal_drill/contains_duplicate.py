def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate_set(nums):
    return len(nums) != len(set(nums))


nums = [1, 2, 3, 4, 1]

print("Contains Duplicate: ", contains_duplicate(nums), contains_duplicate_set(nums))
