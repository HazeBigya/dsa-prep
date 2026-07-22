def three_sum(nums):
    nums.sort()
    n = len(nums)
    output = []
    
    for i in range(0, n-2):
        if i > 0 and nums[i] == nums[i -1]:
            continue
        
        target = -nums[i]
        L = i+1;
        R = n-1;
        
        while L < R:
            sum = nums[L] + nums[R]
            if sum == target:
                output.append([nums[i], nums[L], nums[R]])
                L += 1
                R -= 1
                while L < R and nums[L] == nums[L-1]:
                    L += 1
            elif sum < target:
                L += 1
            else:
                R -= 1
    return output
                
                
nums =  [-1, 0, 1, 2, -1, -4]
print("The Three sum of the array is: ",three_sum(nums))