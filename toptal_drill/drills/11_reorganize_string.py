"""
Toptal Top-20 Target #14 — Reorganize String
Frequency: 67%  |  Difficulty: Medium
Pattern: Heap (max-heap by count) + greedy

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: NEW TOOL: heapq. Warm up heapq basics before this.

Problem:
  Rearrange the string so no two adjacent chars are the same.
  Return any valid arrangement, or '' if impossible.

Approach:
  1. Count chars (Counter). Max-heap by frequency (push -count in Python).
  2. Repeatedly pop the two most frequent, append both, decrement, push back
  3. the ones still > 0. Impossible if the top count > (len+1)//2.

Example:
  s = "aab"  # -> "aba"   ;   s = "aaab"  # -> ""
"""


def reorganizeString(s):
    # TODO: your solution here
    pass
