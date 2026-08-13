# DSA Prep

Data structures & algorithms practice — solved in **TypeScript** and **Python** for cross-language fluency.

Following an 8-week, pattern-based plan (NeetCode 150 / Grind 75 style). See [DSA_Prep_Plan.md](./DSA_Prep_Plan.md) for the full roadmap.

## Approach

Each problem is worked the way an interview tests it:

1. Restate the problem
2. Talk through the approach — brute force first, then optimize
3. Code it clean, narrating the thinking
4. State time & space complexity
5. Redo cold days later (spaced repetition)

## Progress

### Week 1 — Arrays, Hashing, Two Pointers

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| [Two Sum](./two_sum) | ✅ | ✅ | ⏳ pending | Hash map (value → index) | O(n) | O(n) |
| [Contains Duplicate](./contains_duplicate) | ✅ | ✅ | ⏳ pending | Set membership | O(n) | O(n) |
| [Valid Anagram](./valid_anagram) | ✅ | ✅ | ⏳ pending | Char-count map | O(n) | O(1) |
| [Group Anagrams](./group_anagrams) | ✅ | ✅ | ⏳ pending | Canonical-key bucketing (sorted / count) | O(n·k) | O(n·k) |
| [Top K Frequent](./top_k_frequent) | ✅ | ✅ | ⏳ pending | Count map + sort by frequency | O(n log n) | O(n) |
| [Product of Array Except Self](./product_of_array) | ✅ | ✅ | — | Prefix × suffix products (no division) | O(n) | O(1) extra |
| [Two Sum II (sorted)](./two_sum) | ✅ | ✅ | — | Two pointers converge on target (sorted input) | O(n) | O(1) |
| [Container With Most Water](./container_with_most_water) | ✅ | ✅ | — | Two pointers, move the shorter wall (greedy) | O(n) | O(1) |
| [3Sum](./three_sum) | ✅ | ✅ | ⏳ pending | Sort + fix one + two-pointer inner + dedup | O(n²) | O(1) |
| [Valid Palindrome](./is_palindrome) | ✅ | ✅ | — | Two pointers, skip non-alnum on the fly | O(n) | O(1) |

### Week 2 — Sliding Window & Stack

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| [Best Time to Buy/Sell Stock](./best_time_stock) | ✅ | ✅ | — | Track min-so-far, best profit selling today | O(n) | O(1) |
| [Longest Substring Without Repeating](./longest_substring) | ✅ | ✅ | — | Sliding window + set; shrink L on repeat | O(n) | O(min(n,charset)) |
| [Longest Repeating Character Replacement](./char_replacement) | ✅ | ✅ | — | Sliding window; valid if `windowLen − maxFreq ≤ k` | O(n) | O(26) |
| [Valid Parentheses](./valid_parentheses) | ✅ | ✅ | — | Stack (LIFO); map closer→opener, pop & match | O(n) | O(n) |
| [Min Stack](./min_stack) | ✅ | ✅ | — | Parallel min-stack; push min-so-far, pop together | O(1) all ops | O(n) |
| [Evaluate RPN](./eval_rpn) | ✅ | ✅ | — | Stack; push nums, operator pops 2 & pushes result | O(n) | O(n) |
| [Daily Temperatures](./daily_temperatures) | ✅ | ✅ | — | Monotonic stack of indices; pop when warmer, gap = i−idx | O(n) | O(n) |
| [Car Fleet](./car_fleet) | ✅ | ✅ | — | Sort by pos desc; stack of arrival times; new fleet if time > top | O(n log n) | O(n) |
| [Minimum Window Substring](./min_window_substring) 🔴 | ✅ | ✅ | — | Variable window; need/have counter; grow to valid, shrink to min | O(s+t) | O(t) |
| [Largest Rectangle in Histogram](./largest_rectangle) | ✅ | ✅ | — | Monotonic stack of indices; pop taller, width = i−stack[-1]−1, drain with n | O(n) | O(n) |

### Week 3 — Binary Search & Linked Lists

Not started. `⬜` = to do. Drill column marks Toptal-drill reps done in `toptal_drill/` (`⏳ pending` = drilled once, cold-redo owed; `✅` = drilled + cold-redo locked).

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Binary Search | ⬜ | ⬜ | — | — | — | — |
| Search a 2D Matrix | ⬜ | ⬜ | — | — | — | — |
| Koko Eating Bananas | ⬜ | ⬜ | — | — | — | — |
| Find Minimum in Rotated Sorted Array | ⬜ | ⬜ | — | — | — | — |
| Search in Rotated Sorted Array | ⬜ | ⬜ | — | — | — | — |
| Reverse Linked List | ⬜ | ⬜ | — | — | — | — |
| Merge Two Sorted Lists | ⬜ | ⬜ | — | — | — | — |
| Reorder List | ⬜ | ⬜ | — | — | — | — |
| Remove Nth Node From End | ⬜ | ⬜ | — | — | — | — |
| Linked List Cycle | ⬜ | ⬜ | — | — | — | — |
| Add Two Numbers | ⬜ | ⬜ | — | — | — | — |

### Week 4 — Trees (the big one)

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Invert Binary Tree | ⬜ | ⬜ | — | — | — | — |
| Maximum Depth of Binary Tree | ⬜ | ⬜ | ✅ | DFS, `max(left,right)+1` | O(n) | O(h) |
| Diameter of Binary Tree | ⬜ | ⬜ | ✅ | DFS returns height, track best | O(n) | O(h) |
| Balanced Binary Tree | ⬜ | ⬜ | — | — | — | — |
| Same Tree | ⬜ | ⬜ | — | — | — | — |
| Subtree of Another Tree | ⬜ | ⬜ | — | — | — | — |
| Lowest Common Ancestor of a BST | ⬜ | ⬜ | — | — | — | — |
| Binary Tree Level Order Traversal | ⬜ | ⬜ | ⏳ pending | BFS + `deque`, row-size snapshot | O(n) | O(n) |
| Validate Binary Search Tree | ⬜ | ⬜ | — | — | — | — |
| Kth Smallest Element in a BST | ⬜ | ⬜ | — | — | — | — |
| Construct Tree from Preorder and Inorder | ⬜ | ⬜ | — | — | — | — |

### Week 5 — Tries, Heaps / Priority Queue, Backtracking

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Implement Trie (Prefix Tree) | ⬜ | ⬜ | — | — | — | — |
| Design Add and Search Words Data Structure | ⬜ | ⬜ | — | — | — | — |
| Kth Largest Element in a Stream | ⬜ | ⬜ | — | — | — | — |
| Last Stone Weight | ⬜ | ⬜ | — | — | — | — |
| K Closest Points to Origin | ⬜ | ⬜ | — | — | — | — |
| Task Scheduler | ⬜ | ⬜ | — | — | — | — |
| Subsets | ⬜ | ⬜ | — | — | — | — |
| Combination Sum | ⬜ | ⬜ | — | — | — | — |
| Permutations | ⬜ | ⬜ | — | — | — | — |
| Word Search | ⬜ | ⬜ | — | — | — | — |

### Week 6 — Graphs (critical for system-y roles)

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Number of Islands | ⬜ | ⬜ | — | — | — | — |
| Clone Graph | ⬜ | ⬜ | — | — | — | — |
| Pacific Atlantic Water Flow | ⬜ | ⬜ | — | — | — | — |
| Course Schedule (topological sort) | ⬜ | ⬜ | — | — | — | — |
| Course Schedule II | ⬜ | ⬜ | — | — | — | — |
| Graph Valid Tree | ⬜ | ⬜ | — | — | — | — |
| Number of Connected Components | ⬜ | ⬜ | — | — | — | — |
| Rotting Oranges | ⬜ | ⬜ | — | — | — | — |
| Walls and Gates | ⬜ | ⬜ | — | — | — | — |
| Word Ladder | ⬜ | ⬜ | — | — | — | — |

### Week 7 — Dynamic Programming (1D + intro 2D)

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Climbing Stairs | ⬜ | ⬜ | — | — | — | — |
| Min Cost Climbing Stairs | ⬜ | ⬜ | — | — | — | — |
| House Robber | ⬜ | ⬜ | — | — | — | — |
| House Robber II | ⬜ | ⬜ | — | — | — | — |
| Longest Palindromic Substring | ⬜ | ⬜ | — | — | — | — |
| Palindromic Substrings | ⬜ | ⬜ | — | — | — | — |
| Decode Ways | ⬜ | ⬜ | — | — | — | — |
| Coin Change | ⬜ | ⬜ | — | — | — | — |
| Maximum Product Subarray | ⬜ | ⬜ | — | — | — | — |
| Longest Increasing Subsequence | ⬜ | ⬜ | — | — | — | — |
| Unique Paths (2D) | ⬜ | ⬜ | — | — | — | — |
| Longest Common Subsequence (2D) | ⬜ | ⬜ | — | — | — | — |

### Week 8 — Greedy, Intervals, Mixed Review + Mock Interviews

| Problem | TS | Python | Drill | Pattern | Time | Space |
|---------|----|--------|-------|---------|------|-------|
| Maximum Subarray (Kadane's) | ⬜ | ⬜ | ⏳ pending | Kadane — `max(fresh, extend)`, seed best=nums[0] | O(n) | O(1) |
| Jump Game | ⬜ | ⬜ | — | — | — | — |
| Insert Interval | ⬜ | ⬜ | — | — | — | — |
| Merge Intervals | ⬜ | ⬜ | — | — | — | — |
| Non-overlapping Intervals | ⬜ | ⬜ | — | — | — | — |

### Fundamentals / Warmups

Classic phone-screen warmups (not NeetCode 150, but frequently asked).

| Problem | TS | Python | Pattern | Time | Space |
|---------|----|--------|---------|------|-------|
| [Fibonacci](./fundamentals/febonacci) | ✅ | ✅ | Iterative — series (array) + nth value (two-var slide) | O(n) | O(n) series / O(1) value |
| [Prime Check](./fundamentals/prime) | ✅ | ✅ | Trial division to √n (`i*i <= n`) | O(√n) | O(1) |
| [Factorial](./fundamentals/factorial) | ✅ | ✅ | Recursive (base + shrink) + iterative | O(n) | O(n) rec / O(1) iter |
| [Sorting](./fundamentals/sorting) | ✅ | ✅ | Built-in (asc/desc, array + string) + manual bubble | O(n log n) built-in / O(n²) bubble | O(1) |
| [Reverse](./fundamentals/reverse) | ✅ | ✅ | Two-pointer swap ends inward (string + array) | O(n) | O(1) |
| [FizzBuzz](./fundamentals/fizzbuzz) | ✅ | ✅ | Modulo, most-specific-first (%15 before %3/%5) | O(n) | O(n) |
| [Digits (sum + count)](./fundamentals/digits) | ✅ | ✅ | Peel digits with `% 10` + `// 10`, no string | O(d) | O(1) |
| [Palindrome Number](./fundamentals/palindrome_number) | ✅ | ✅ | Reverse int via math (`rev*10+digit`), compare | O(d) | O(1) |
| [Max / Min in Array](./fundamentals/max_min) | ✅ | ✅ | Single pass, seed from `nums[0]` (not 0) | O(n) | O(1) |
| [GCD / LCM](./fundamentals/gcd_lcm) | ✅ | ✅ | Euclid: `gcd(a,b)=gcd(b,a%b)`; `lcm=a*b/gcd` | O(log min(a,b)) | O(1) |

### System Design

Co-equal track with the coding work — one design/week, laddered easy→hard. Format is reasoning + tradeoffs + ASCII diagrams (not code), each exported to PDF. Core drill: defend every choice against the obvious alternative. Terms surfaced go in [VOCAB_MAP.md](./VOCAB_MAP.md).

| Design | Doc | PDF | Focus |
|--------|-----|-----|-------|
| [URL Shortener](./system_design/url_shortener/design.md) | ✅ | ✅ | Read-heavy, 302 vs 301, base62 codes, cache-aside, async counter, hot-key |

Planned: Rate Limiter · Pastebin/Image Host · Web Crawler · Chat/Messaging · News Feed · Video Streaming · Ticketing (concurrency) · RAG/LLM Serving. Plus LLD: Elevator, Parking Lot. See [DSA_Prep_Plan.md](./DSA_Prep_Plan.md).

### Drills — Toptal Sprint (Python only)

Timed, narrated cold-redos — solved fresh (no peeking), approach explained out loud like a live interview. Split into **foundations** (base rungs) and **target drills** (the Most-Asked Top 20). Files are numbered by priority (`01` = highest). Live status index: [toptal_drill/ROADMAP.md](./toptal_drill/ROADMAP.md).

**Status: 11 target drills done · 6 to do.** Next ⬜ = lowest-numbered todo.

#### 🪜 Foundations — `toptal_drill/foundations/` *(all done)*

| # | Problem | Pattern | Holds up |
|---|---------|---------|----------|
| 01 | [Two Sum](./toptal_drill/foundations/01_two_sum.py) | Hash map (complement lookup) | Hash-map ladder |
| 02 | [Valid Anagram](./toptal_drill/foundations/02_valid_anagram.py) | Char-count maps compared | Hash-map ladder |
| 03 | [Group Anagrams](./toptal_drill/foundations/03_group_anagrams.py) | Canonical-key bucketing | Hash-map ladder |
| 04 | [Contains Duplicate](./toptal_drill/foundations/04_contains_duplicate.py) | Set membership, early exit | Hash-map ladder |
| 05 | [Maximum Subarray](./toptal_drill/foundations/05_maximum_subarray.py) | Kadane — `max(fresh, extend)` | → drill 09 |
| 06 | [Maximum Depth of Binary Tree](./toptal_drill/foundations/06_maximum_depth_binary_tree.py) | DFS; `max(left,right)+1` | → drills 04, 13 |
| 07 | [Level Order Traversal](./toptal_drill/foundations/07_level_order_traversal.py) | BFS + `deque`, row-size snapshot | → drill 13, graph |
| 08 | [Number of Islands](./toptal_drill/foundations/08_number_of_islands.py) | DFS flood-fill, sink-to-0 | → drills 06, 12 |
| 09 | [heapq basics](./toptal_drill/foundations/09_heap_basics.py) | Min-heap, negate-for-max, tuple ordering | → drills 11, 16 |
| 10 | [Difference Array](./toptal_drill/foundations/10_difference_array.py) | `diff[l]+=v`, `diff[r+1]-=v`, prefix-sum | → drill 07 |
| 11 | [Monotonic Deque](./toptal_drill/foundations/11_monotonic_deque.py) | Window max/min at the front, O(1) | → drill 08 |

#### 🎯 Target Drills — `toptal_drill/drills/` (Top 20, ranked by frequency)

| # | Problem | Freq | Pattern | Status |
|---|---------|------|---------|--------|
| 01 | [Invalid Transactions](./toptal_drill/drills/01_invalid_transactions.py) | 100% | Group by name + inner conflict scan | ✅ |
| 02 | [Subarray Sum Equals K](./toptal_drill/drills/02_subarray_sum_equals_k.py) | 92% | Prefix sum + hashmap of seen sums | ✅ |
| 03 | [3Sum](./toptal_drill/drills/03_three_sum.py) | 90% | Sort + fix one + two-pointer + dedup | ✅ |
| 04 | [Diameter of Binary Tree](./toptal_drill/drills/04_diameter_binary_tree.py) | 90% | DFS returns height, track best | ✅ |
| 05 | [Isomorphic Strings](./toptal_drill/drills/05_isomorphic_strings.py) | 88% | Two-way map (or map + used set) | ✅ |
| 06 | [Accounts Merge](./toptal_drill/drills/06_accounts_merge.py) | 82% | Union-find / DFS on emails | ✅ |
| 07 | [Zero Array Transformation II](./toptal_drill/drills/07_zero_array_transformation.py) | 76% | Difference array + binary search on answer | ✅ |
| 08 | [Continuous Subarrays](./toptal_drill/drills/08_continuous_subarrays.py) | 75% | Window + monotonic deques | ⬜ |
| 09 | [Maximum Sum Circular Subarray](./toptal_drill/drills/09_maximum_circular_subarray.py) | 75% | Kadane ×2; `wrap = total − minSum` | ✅ |
| 10 | [Largest Rectangle](./toptal_drill/drills/10_largest_rectangle.py) | 73% | Monotonic stack *(done in Week 2)* | ✅ |
| 11 | [Reorganize String](./toptal_drill/drills/11_reorganize_string.py) | 67% | Max-heap by count + greedy | ✅ |
| 12 | [Number of Distinct Islands](./toptal_drill/drills/12_distinct_islands.py) | 63% | DFS flood + relative-offset shape sig | ✅ |
| 13 | [Vertical Order Traversal](./toptal_drill/drills/13_vertical_order_traversal.py) | 61% | BFS + `(node, col)` pairs + column map | ✅ |
| 14 | [Top K Frequent](./toptal_drill/drills/14_top_k_frequent.py) | 61% | Counter + bucket sort by frequency | ✅ |
| 15 | [Check If N and Its Double Exist](./toptal_drill/drills/15_check_n_double.py) | 61% | One-pass set, check `2x` and `x/2` | ✅ |
| 16 | [Find K Pairs with Smallest Sums](./toptal_drill/drills/16_find_k_pairs.py) | 57% | Min-heap frontier (k-way merge) | ⬜ |
| 17 | [Combination Sum II](./toptal_drill/drills/17_combination_sum_ii.py) | 57% | Backtracking with dedup | ⬜ |

⏭️ **Skipped** (rare + Hard, low ROI): #7 Rank Transform of a Matrix · #11 Bus Routes · #13 Median of Two Sorted Arrays.

See [TOPTAL_PREP.md](./TOPTAL_PREP.md) for the full ladder map + schedule.

## Structure

```
<problem_name>/
  <problem_name>.ts     # TypeScript solution
  <problem_name>.py     # Python solution

system_design/
  <design_name>/
    design.md           # reasoning, tradeoffs, ASCII diagrams
    <design_name>.pdf   # exported PDF
```

## Running

```bash
# TypeScript
npx tsx two_sum/two_sum.ts

# Python
python3 two_sum/two_sum.py
```
