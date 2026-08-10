"""
Toptal Top-20 Target #9 — Continuous Subarrays
Frequency: 75%  |  Difficulty: Medium
Pattern: Sliding window + monotonic deque (min & max in window)

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: window skeleton from Week 2 longest_substring; deque from BFS

Problem:
  Count subarrays where max(subarray) - min(subarray) <= 2.
  A window is valid while its (max - min) stays within 2; count all
  subarrays ending at each right index.

Approach:
  1. Expand R; keep a max-deque and a min-deque over the window.
  2. While window invalid (maxDeque.front - minDeque.front > 2) shrink L.
  3. Add (R - L + 1) to the count each step.

Example:
  nums = [5,4,2,4]  # -> 8
"""


def continuousSubarrays(nums):
    # TODO: your solution here
    pass
