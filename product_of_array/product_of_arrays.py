def product_of_array(nums):
    n = len(nums)
    output = [1] * n
    
    pre = 1
    for i in range(n):
        output[i] = pre
        pre *= nums[i]
        
    post = 1
    for i in range(n-1, -1, -1):
        output[i] *= post
        post *= nums[i]
        
    return output

nums = [1, 2, 3, 4]
print("The product of array except self is:", product_of_array(nums))