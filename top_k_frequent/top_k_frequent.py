def topKFrequent(nums, k):
    frequency_map = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    sorted_entries = sorted(frequency_map.items(), key=lambda x: x[1], reverse=True)
    return [entry[0] for entry in sorted_entries[:k]]   