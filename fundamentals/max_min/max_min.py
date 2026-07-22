def max_min(nums):
    max = nums[0]
    min = nums[0]
    
    for i in range (1, len(nums)):
        if nums [i] > max: max = nums[i]
        if nums [i] < min: min = nums[i]
    
    print(f"The Max number is {max} and the min number is {min}")
    
nums = [4, 6, -2, 9, -7, 6]
max_min(nums)