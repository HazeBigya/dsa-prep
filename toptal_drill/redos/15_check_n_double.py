def check_n_double(nums):
    seen = set()
    for num in nums:
        if num * 2 in seen or num / 2 in seen:
            return True
        seen.add(num)

    return False
