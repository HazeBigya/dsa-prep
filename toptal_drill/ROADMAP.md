# Toptal Drill Roadmap

Files are **numbered by priority** (`01` = highest). Lowest-numbered ⬜ = do next.
`✅` solved · `⬜` TODO (stub file ready — solve from scratch, out loud, then cold-redo).

## 🎯 `drills/` — Top-20 Target Problems (ranked by reported frequency)

| Rank | Problem | Freq | Diff | Status |
|------|---------|------|------|--------|
| 01 | Invalid Transactions | 100% | Med | ✅ |
| 02 | Subarray Sum Equals K | 92% | Med | ✅ |
| 03 | 3Sum | 90% | Med | ✅ |
| 04 | Diameter of Binary Tree | 90% | Easy | ✅ |
| 05 | Isomorphic Strings | 88% | Easy | ✅ |
| 06 | **Accounts Merge** | 82% | Med | ✅ *(union-find — cold redo done 2026-08-12)* |
| 07 | Zero Array Transformation II | 76% | Med | ⬜ |
| 08 | Continuous Subarrays | 75% | Med | ⬜ |
| 09 | Maximum Sum Circular Subarray | 75% | Med | ✅ |
| 10 | Largest Rectangle in Histogram | 73% | Hard | ✅ *(done in Week 2 `../largest_rectangle/`)* |
| 11 | Reorganize String | 67% | Med | ✅ *(max-heap greedy — solved + cold redo 2026-08-12; first heap)* |
| 12 | Number of Distinct Islands | 63% | Med | ✅ |
| 13 | Vertical Order Traversal | 61% | Med | ✅ |
| 14 | Top K Frequent Elements | 61% | Med | ✅ |
| 15 | Check If N and Its Double Exist | 61% | Easy | ✅ |
| 16 | Find K Pairs with Smallest Sums | 57% | Med | ⬜ *(new tool: heapq)* |
| 17 | Combination Sum II | 57% | Med | ⬜ *(new pattern: backtracking)* |

**Done: 13 · TODO: 4**

### ⏭️ Skipped (rare + Hard, low ROI before Aug 18)
#7 Rank Transform of a Matrix · #11 Bus Routes · #13 Median of Two Sorted Arrays

## 🪜 `foundations/` — Base Rungs (not top-20; hold up the targets)

| # | Problem | Holds up | Status |
|---|---------|----------|--------|
| 01 | Two Sum | Hash Map ladder | ✅ |
| 02 | Valid Anagram | Hash Map ladder | ✅ |
| 03 | Group Anagrams | Hash Map ladder | ✅ |
| 04 | Contains Duplicate | Hash Map ladder | ✅ |
| 05 | Maximum Subarray (Kadane) | → drill 09 | ✅ |
| 06 | Maximum Depth of Binary Tree | → drills 04, 13 | ✅ |
| 07 | Level Order Traversal (BFS) | → drill 13, graph | ✅ |
| 08 | Number of Islands (flood) | → drills 06, 12 | ✅ |
| 09 | heapq basics (min-heap, negate-for-max, tuples) | → drills 11, 16 | ✅ |

## Owed cold-redos (spaced)
- _(none — all cleared 2026-08-12: #6 Accounts Merge, #9 Circular Subarray, foundations/05 Kadane, #12 Distinct Islands all cold-redone)_
