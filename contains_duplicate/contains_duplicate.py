def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def containsDuplicateOneLine(nums):
    return len(nums) != len(set(nums))

# Example usage
nums = [1, 2, 3, 4, 5, 1]
result = containsDuplicate(nums)
print("Contains duplicate:", result)  # Output: True

oneliner_result = containsDuplicateOneLine(nums)
print("Contains duplicate (one-liner):", oneliner_result)  # Output: