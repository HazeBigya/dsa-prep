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

### Drills

Timed, narrated cold-redos in Python — solved fresh (no peeking at old solutions), explaining the approach out loud like a live interview. Interview-fluency practice, not new material.

Organized as **foundation → target ladders**: master the foundation rung, then climb to the higher-frequency target that stands on it. `★` = a top-asked target problem.

**Ladder 1 — Hash Map / Set** *(complete)*

| Problem | Rung | Pattern | Time | Space |
|---------|------|---------|------|-------|
| [Two Sum](./toptal_drill/foundations/01_two_sum.py) | foundation | Hash map (complement lookup) | O(n) | O(n) |
| [Valid Anagram](./toptal_drill/foundations/02_valid_anagram.py) | foundation | Char-count maps compared | O(n) | O(n) |
| [Group Anagrams](./toptal_drill/foundations/03_group_anagrams.py) | foundation | Canonical-key bucketing (sorted key) | O(n·k log k) | O(n·k) |
| [Contains Duplicate](./toptal_drill/foundations/04_contains_duplicate.py) | foundation | Set membership, early exit | O(n) | O(n) |
| [Top K Frequent](./toptal_drill/drills/14_top_k_frequent.py) ★ | target | Counter + bucket sort by frequency | O(n) | O(n) |
| [Isomorphic Strings](./toptal_drill/drills/05_isomorphic_strings.py) ★ | target | Two-way map (or one map + used set) | O(n) | O(n) |
| [Check If N and Its Double Exist](./toptal_drill/drills/15_check_n_double.py) ★ | target | One-pass set, check `2x` and `x/2` | O(n) | O(n) |
| [Invalid Transactions](./toptal_drill/drills/01_invalid_transactions.py) ★ | target | Group by name + inner conflict scan | O(n²) | O(n) |

**Ladder 2 — Prefix Sum** *(complete)*

| Problem | Rung | Pattern | Time | Space |
|---------|------|---------|------|-------|
| [Subarray Sum Equals K](./toptal_drill/drills/02_subarray_sum_equals_k.py) ★ | target | Running sum + hashmap of seen sums; count `running − k` | O(n) | O(n) |

**Ladder 3 — Kadane / Max Subarray** *(complete)*

| Problem | Rung | Pattern | Time | Space |
|---------|------|---------|------|-------|
| [Maximum Subarray](./toptal_drill/foundations/05_maximum_subarray.py) | foundation | Kadane — `max(start fresh, extend)`, seed best=nums[0] | O(n) | O(1) |
| [Maximum Sum Circular Subarray](./toptal_drill/drills/09_maximum_circular_subarray.py) ★ | target | Kadane ×2 (max + min); `wrap = total − minSum`; all-neg guard | O(n) | O(1) |

**Ladder 5 — Two-Pointer / Sort**

| Problem | Rung | Pattern | Time | Space |
|---------|------|---------|------|-------|
| [3Sum](./three_sum/three_sum.py) ★ | target | Sort + fix one + two-pointer + dedup | O(n²) | O(n) |

**Ladder 8 — Trees** *(started)*

| Problem | Rung | Pattern | Time | Space |
|---------|------|---------|------|-------|
| [Maximum Depth of Binary Tree](./toptal_drill/foundations/06_maximum_depth_binary_tree.py) | foundation | DFS recursion; `max(left,right)+1`, base `None→0` | O(n) | O(h) |

Next ladders in queue: Trees targets (Diameter #4, Vertical Order #16), then Heap / Graph basics. See [TOPTAL_PREP.md](./TOPTAL_PREP.md) for the full ladder map + schedule.

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
