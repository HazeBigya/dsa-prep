def bucket_sort(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in frequency_map.items():
        buckets[freq].append(num)
    
    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                print("Final Result:", result)
                return result
        
        
nums = [1, 1, 1, 2, 2, 3]
k = 2
print("The top", k, "frequent elements are:", bucket_sort(nums, k))        
    