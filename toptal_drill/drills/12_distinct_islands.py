"""
Toptal Top-20 Target #15 — Number of Distinct Islands
Frequency: 63%  |  Difficulty: Medium
Pattern: DFS flood + canonical shape signature

STATUS: TODO (roadmap stub — solve from scratch, out loud, then cold-redo)
Foundation: STANDS ON foundations/08_number_of_islands.py (do that first)

Problem:
  Count islands with DISTINCT shapes (translation-invariant). Two islands
  are the same if one can shift onto the other (no rotation/reflection).

Approach:
  1. For each island, DFS-flood it (like Number of Islands) BUT record the
  2. path shape: append each step's direction ('U/D/L/R' + a backtrack mark)
  3. OR each cell offset relative to the start. Store signatures in a set;
  4. answer = len(set).

Example:
  two identical L-shapes in different spots -> 1 distinct
"""


def numDistinctIslands(grid):
    # TODO: your solution here
    pass
