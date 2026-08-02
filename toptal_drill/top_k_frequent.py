from collections import Counter


def top_k_frequent(nums, k):
    freq_map = Counter(nums)
    common = freq_map.most_common(k)
    res = []
    # for num, freq in common:
    #     res.append(num)
    # return res
    return [elem for elem, _ in common]


def top_k_frequent_bucket_sort(nums, k):
    freq_map = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, freq in freq_map.items():
        buckets[freq].append(num)

    res = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res

    return res


nums = [2, 2, 2, 1, 1, 3, 3, 4]
k = 2

print(f"The top {k} frequent items are: {top_k_frequent(nums, k)}")
print(
    f"The top {k} frequent items using bucket sort are: {top_k_frequent_bucket_sort(nums, k)}"
)
