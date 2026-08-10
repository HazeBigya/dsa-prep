"""
Toptal Top-20 Target #20 — Combination Sum II
Frequency: 57%  |  Difficulty: Medium
Pattern: Backtracking with dedup

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: NEW PATTERN: backtracking (lowest priority; only if time)

Problem:
  Given candidates (may repeat) and target, return all UNIQUE combos that
  sum to target. Each number used at most once. No duplicate combos.

Approach:
  1. Sort candidates. Backtrack from a start index; skip a value equal to
  2. its left neighbor at the same depth (dedup). Recurse with i+1 (use once).

Example:
  candidates=[10,1,2,7,6,1,5], target=8  # -> [[1,1,6],[1,2,5],[1,7],[2,6]]
"""


def combinationSum2(candidates, target):
    # TODO: your solution here
    pass
