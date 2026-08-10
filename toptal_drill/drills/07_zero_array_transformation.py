"""
Toptal Top-20 Target #8 — Zero Array Transformation II
Frequency: 76%  |  Difficulty: Medium
Pattern: Greedy + difference array (range updates)

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: prefix-sum idea from drills/02_subarray_sum_equals_k.py

Problem:
  queries[i] = [l, r, val]; each may decrement every nums[j] in [l,r] by
  at most val. Find the MIN number of queries (prefix of the list) needed
  to make nums all zeros. Return -1 if impossible with all queries.

Approach:
  1. Binary-search the answer k, OR sweep with a difference array tracking
  2. how much decrement is available at each index (running sum of deltas).
  3. Diff array: apply +val at l, -val at r+1; prefix-sum gives coverage.

Example:
  nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]  # -> 2
"""


def minZeroArray(nums, queries):
    # TODO: your solution here
    pass
