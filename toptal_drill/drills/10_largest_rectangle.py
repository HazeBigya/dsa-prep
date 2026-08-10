"""
Toptal Top-20 Target #12 — Largest Rectangle in Histogram
Frequency: 73%  |  Difficulty: Hard
Pattern: Monotonic stack of indices

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: done via Week 2 stack ladder

Problem:
  *** ALREADY DONE in Week 2 -> see ../../largest_rectangle/ ***
  Listed here only to keep the top-20 roadmap complete.
  Cold-redo target if you want the rep fresh.

Approach:
  1. Monotonic increasing stack of indices; when a shorter bar appears, pop
  2. and compute area = poppedHeight * (i - stack[-1] - 1). Drain with n.

Example:
  heights = [2,1,5,6,2,3]  # -> 10
"""


def largestRectangleArea(heights):
    # TODO: your solution here
    pass
