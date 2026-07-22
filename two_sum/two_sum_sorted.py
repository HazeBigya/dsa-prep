def two_sum_sorted(nums, target):
    L = 0
    R = len(nums) - 1
    while( L < R):
        sum = nums[L] + nums[R]
        if(sum == target):
            return [L+1, R+1]
        elif(sum < target):
            L += 1
        else:
            R -= 1

nums = [2, 7, 9, 11, 15, 20, 31];
target = 35;

print("The sum of array for target ",target," is ", two_sum_sorted(nums, target))
