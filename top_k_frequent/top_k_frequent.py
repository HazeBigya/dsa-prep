from collections import Counter

def topKFrequent(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    sorted_entries = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    return [entry[0] for entry in sorted_entries[:k]]   

def topKFrequentUsingCounter(nums, k):
    frequency_map = Counter(nums)
    common = frequency_map.most_common(k)
    return [element for element, _ in common]

nums = [1, 1, 1, 2, 2, 3]   
k = 2
result = topKFrequent(nums, k)
counter_result = topKFrequentUsingCounter(nums, k)

print("The top", k, "frequent elements are:", result);
print("Using Counter:", counter_result);