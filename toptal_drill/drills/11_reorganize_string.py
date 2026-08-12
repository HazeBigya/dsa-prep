import heapq
from collections import Counter


def reorganizeString(s):
    char_count = Counter(s)
    heap = []

    for char, count in char_count.items():
        heap.append((-count, char))
    heapq.heapify(heap)

    result = []

    while len(heap) >= 2:
        count1, char1 = heapq.heappop(heap)
        count2, char2 = heapq.heappop(heap)

        result.extend([char1, char2])

        count1 += 1
        count2 += 1

        if count1 < 0:
            heapq.heappush(heap, (count1, char1))

        if count2 < 0:
            heapq.heappush(heap, (count2, char2))

    if heap:
        count, char = heapq.heappop(heap)
        if -count > 1:
            return ""
        result.append(char)

    return "".join(result)


s = "aab"
print(reorganizeString(s))
