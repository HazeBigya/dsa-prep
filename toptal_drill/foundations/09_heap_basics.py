"""
Foundation #09 — heapq basics (warm-up before drills 11 & 16)

Goal: learn the ONLY 4 heapq calls, on plain numbers, before tuples/negation.
A heap = structure that always hands you the SMALLEST item in O(log n).
Python has ONLY a min-heap. (max-heap = negate the values — Part 3.)

Fill each ___ , PREDICT the print in the comment, THEN run:  python 09_heap_basics.py
"""

import heapq


# ── Part 1: push then pop — watch sorted order fall out ──────────────────
# heappush adds; heappop removes+returns the SMALLEST. Root is always min.
def part1():
    h = []
    for x in [5, 1, 8, 3]:
        heapq.heappush(h, x)  # push each number
    out = []
    while h:
        out.append(heapq.heappop(h))  # pop smallest until empty
    print("part1:", out)
    # PREDICT: out = [1, 3, 5, 8]


# ── Part 2: heapify — turn an existing list into a heap in place, O(n) ────
def part2():
    nums = [9, 4, 7, 1, 2]
    heapq.heapify(nums)  # heapify in place
    print("part2 root (smallest):", nums[0])
    # PREDICT: nums[0] = 1
    # (note: nums is NOT fully sorted after heapify — only nums[0] is guaranteed min)


# ── Part 3: MAX-heap via negation (the drill-11 trick) ───────────────────
# Push -x. The most-negative pops first = the largest real value.
# Remember to negate AGAIN when you read it back.
def part3():
    h = []
    for x in [5, 1, 8, 3]:
        heapq.heappush(h, -x)  # push the NEGATION of x
    biggest = -heapq.heappop(h)  # pop, then flip the sign back to positive
    print("part3 biggest:", biggest)
    # PREDICT: biggest = 8


# ── Part 4: tuples — heap orders by the FIRST element (drill-11 shape) ────
# This is exactly (-count, char) from Reorganize String.
def part4():
    h = [(-2, "a"), (-1, "b"), (-3, "c")]
    heapq.heapify(h)
    count, char = heapq.heappop(h)  # what pops first?
    print("part4 first out:", char, "with real count", -count)
    # PREDICT: char = c , real count = 3


# ── Part 5: mini-drill — return the K LARGEST numbers ────────────────────
# Use a max-heap (negation). Pop k times.
def kLargest(nums, k):
    h = []
    for x in nums:
        heapq.heappush(h, -x)  # max-heap: push negation
    result = []
    for _ in range(k):
        result.append(-heapq.heappop(h))  # pop and flip sign back
    return result
    # (heapq.nlargest(k, nums) exists too — but do it by hand here to feel the tool)


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    print("part5 kLargest([5,1,8,3,9], 2):", kLargest([5, 1, 8, 3, 9], 2))
    # PREDICT: [9, 8]
