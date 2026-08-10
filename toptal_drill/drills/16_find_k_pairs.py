"""
Toptal Top-20 Target #19 — Find K Pairs with Smallest Sums
Frequency: 57%  |  Difficulty: Medium
Pattern: Min-heap (k-way merge frontier)

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: NEW TOOL: heapq (do 11_reorganize_string first to warm heapq)

Problem:
  Given sorted nums1, nums2 and k, return the k pairs (a,b) with the
  smallest sums a+b.

Approach:
  1. Min-heap seeded with (nums1[i]+nums2[0], i, 0) for first few i.
  2. Pop smallest, push its right neighbor (i, j+1). Repeat k times.

Example:
  nums1=[1,7,11], nums2=[2,4,6], k=3  # -> [[1,2],[1,4],[1,6]]
"""


def kSmallestPairs(nums1, nums2, k):
    # TODO: your solution here
    pass
