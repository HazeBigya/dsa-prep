"""
Toptal Target #17 — Combination Sum II
Difficulty: Medium  |  Pattern: backtracking with duplicate-skip

WORKED SOLUTION + derivation (study, don't memorize).

=============================================================================
THE QUESTION
=============================================================================
candidates may CONTAIN DUPLICATES. Find all UNIQUE combinations that sum to
target. Each candidate may be used AT MOST ONCE (by its position). The result
must not contain duplicate combinations.

    candidates = [10,1,2,7,6,1,5], target = 8
    -> [[1,1,6],[1,2,5],[1,7],[2,6]]

Two separate "no duplicates" rules to keep straight:
  (A) each element used once  -> when you recurse, move START past the one
      you just took (i+1), never reuse the same index.
  (B) no duplicate COMBOS in the output -> even though the array has two 1s,
      [1,7] must appear only once, not once per physical 1.

=============================================================================
HOW THE SOLUTION IS DERIVED
=============================================================================
Backtracking = build a partial combo, go deeper, then UNDO the last choice
and try the next option. A decision tree: at each step choose "which
candidate do I add next", recurse, then pop it back off and move on.

Skeleton of any backtracking solver:
    path = running partial answer
    at each node:
        if path satisfies goal -> record a COPY of path
        else for each next choice:
            add choice to path
            recurse
            remove choice from path   (the "backtrack" / undo)

Now the two problem-specific pieces:

1. "each number once" -> pass a START index. A branch that took index i only
   considers indices i+1.. onward. This also stops permutations: we always
   move forward, so [1,2,5] is generated, never its reordering [2,1,5].

2. "no duplicate combos" -> SORT first so equal values sit next to each other,
   then at a given depth SKIP a value equal to its left neighbor:
        if i > start and candidates[i] == candidates[i-1]: continue
   Read it carefully:
     - i > start  means "not the first choice at THIS depth". The first time
       we see a value at this level we MUST use it (that's how [1,1,6] gets
       its leading 1). We only skip the 2nd, 3rd... identical sibling, because
       starting a branch with the second 1 would rebuild an identical subtree
       to the one the first 1 already made.
     - It skips duplicates ACROSS branches (siblings), NOT down a branch —
       using i+1 in the recursive call still lets [1,1,6] use both 1s in
       sequence.

3. Pruning (optional but natural): sorted array means once
   candidates[i] > remaining, every later candidate is also too big -> break.

=============================================================================
BIG-O
=============================================================================
  Time : O(2^n) worst case -- each element is in/out of a subset, a binary
         decision tree of subsets. (times O(target/min) copy cost per hit;
         usually quoted as O(2^n).) Sorting is O(n log n), dominated.
  Space: O(n) for the recursion depth + the current path (output excluded by
         convention; the results list itself can be exponential).
"""


def combinationSum2(candidates, target):
    candidates.sort()               # rule (B) relies on equal values adjacent
    results = []
    path = []                       # current partial combination

    def backtrack(start, remaining):
        if remaining == 0:          # exact hit -> save a COPY (path keeps mutating)
            results.append(path[:])
            return

        for i in range(start, len(candidates)):
            # skip a duplicate value at the SAME depth (2nd+ identical sibling)
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            # sorted -> this one already overshoots, so do all later ones -> stop
            if candidates[i] > remaining:
                break

            path.append(candidates[i])                 # choose
            backtrack(i + 1, remaining - candidates[i])  # i+1 -> use each once
            path.pop()                                  # un-choose (backtrack)

    backtrack(0, target)
    return results


# --------------------------------------------------------------------------
# self-tests
# --------------------------------------------------------------------------
if __name__ == "__main__":
    def check(got, exp):
        # order-independent compare
        norm = sorted(sorted(c) for c in got)
        exp = sorted(sorted(c) for c in exp)
        print("PASS" if norm == exp else "FAIL", "got", norm, "exp", exp)

    check(combinationSum2([10, 1, 2, 7, 6, 1, 5], 8),
          [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]])
    check(combinationSum2([2, 5, 2, 1, 2], 5),
          [[1, 2, 2], [5]])
    check(combinationSum2([1, 1, 1, 1], 2),
          [[1, 1]])                       # dedup: only ONE [1,1]
    check(combinationSum2([3, 4, 5], 100), [])   # impossible
    check(combinationSum2([1], 1), [[1]])
