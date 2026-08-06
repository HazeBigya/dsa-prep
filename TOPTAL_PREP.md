# Toptal Live Coding — Prep Plan

**Interview:** Tue Aug 18 2026, 5:45–6:45pm (Asia/Kathmandu), Zoom w/ Oscar.
**Format:** 60 min live coding, screen-share, senior engineer watches + you explain aloud.
**Language:** Python only (stdlib + console — confirmed allowed).
**Difficulty:** easy → medium. NOT the brutal Codility auto-test (you skipped that).
**The real test:** thinking out loud clearly, calm under pressure. Communication > cleverness.

---

## Why you can ace this (read when nervous)
- The two most-tested Toptal topics are **hash maps** and **array/string manipulation** — you've already built both (Week 1 + 2 done, 10/10 each).
- The actual reported live problems (Group Anagrams, Two Sum, Longest Substring) — **you've already solved all of them.**
- The problems are easy/medium. You're not learning hard new algorithms in 18 days — you're making what you KNOW automatic and smooth.
- Your one gap (articulation under pressure) is a *trainable* skill, and 17 days of narrated reps fixes it.
- **This is a sharpening sprint, not a learn-from-zero one.** You're further along than most candidates walking in.

---

## ⭐ MOST-ASKED — Priority Targets (Top 20, ranked by reported frequency)

The real Toptal-tagged list. Drill these directly. `✅`=already solved (weeks/drills), `⬜`=to do, `⏭️`=skip (rare + hard, low ROI for 18 days). Source: interviewsolver aggregate — mixes Codility+live; your LIVE round skews to the Easy/Medium ones.

| # | Problem | Freq | Diff | Pattern | Status |
|---|---------|------|------|---------|--------|
| 1 | Invalid Transactions | 100% | Med | hash map / parsing | ✅ |
| 2 | Subarray Sum Equals K | 92% | Med | **prefix sum + hashmap** | ✅ |
| 3 | 3Sum | 90% | Med | sort + two-pointer | ✅ |
| 4 | Diameter of Binary Tree | 90% | Easy | tree DFS | ⬜ |
| 5 | Isomorphic Strings | 88% | Easy | hash map (two-way) | ✅ |
| 6 | Accounts Merge | 82% | Med | union-find / graph | ⬜ |
| 7 | Rank Transform of a Matrix | 79% | Hard | union-find | ⏭️ |
| 8 | Zero Array Transformation II | 76% | Med | greedy + diff array | ⬜ |
| 9 | Continuous Subarrays | 75% | Med | sliding window + deque | ⬜ |
| 10 | Maximum Sum Circular Subarray | 75% | Med | **Kadane variant** | ✅ |
| 11 | Bus Routes | 74% | Hard | BFS | ⏭️ |
| 12 | Largest Rectangle in Histogram | 73% | Hard | monotonic stack | ✅ |
| 13 | Median of Two Sorted Arrays | 67% | Hard | binary search | ⏭️ |
| 14 | Reorganize String | 67% | Med | heap + greedy | ⬜ |
| 15 | Number of Distinct Islands | 63% | Med | DFS/BFS grid | ⬜ |
| 16 | Binary Tree Vertical Order Traversal | 61% | Med | tree BFS + map | ⬜ |
| 17 | Top K Frequent Elements | 61% | Med | bucket sort | ✅ |
| 18 | Check If N and Its Double Exist | 61% | Easy | hash set | ✅ |
| 19 | Find K Pairs with Smallest Sums | 57% | Med | heap | ⬜ |
| 20 | Combination Sum II | 57% | Med | backtracking | ⬜ |

**Also already done (further down the 34-list):** Longest Repeating Char Replacement (#28), Minimum Window Substring (#34).

### 18-day attack order on this list (highest ROI first)
1. **Easy hash/array wins** (fast confidence + high freq): Isomorphic Strings (#5), Check N and Double (#18), Diameter of Binary Tree (#4)
2. **Prefix sum + Kadane** (fills your gaps AND top-asked): Subarray Sum Equals K (#2), Maximum Sum Circular Subarray (#10)
3. **Hash-map mediums:** Invalid Transactions (#1), Reorganize String (#14, also heap)
4. **Graph basics** (union-find/DFS — worth 1-2): Accounts Merge (#6), Number of Distinct Islands (#15)
5. **Heap:** Find K Pairs (#19) — after Reorganize warms up heapq
6. **Skip unless time:** all Hards marked ⏭️, Combination Sum II (backtracking, lower freq)

Realistic: nail the ~12 Easy/Medium ⬜ items + your 3 done = strong coverage. Don't chase the Hards.

## 🪜 Foundation → Target Ladders (HOW to practice)

Don't pick "tiers OR top-20" — climb each **pattern ladder**: do the foundation (often already ✅), then the top-20 target that stands on it. Never attempt a target with a shaky foundation. `✅`=done, `⬜`=to do, `🔁`=done but needs a cold redo first.

### Ladder 1 — Hash Map  (your strongest; fast wins)
`Two Sum ✅` → `Valid Anagram ✅` → `Contains Duplicate ✅`
  ↳ **Isomorphic Strings ✅** (#5, two-way map, two-map version locked; set version had a nested-if bug to fix)
  ↳ **Check If N and Its Double Exist ✅** (#18, hash set, one-pass both-directions)
  ↳ **Invalid Transactions ✅** (#1, group-by-name + inner conflict scan — LADDER 1 COMPLETE)

### Ladder 2 — Prefix Sum  (GAP → high value)
`(new) understand running sum` → `(new) simple subarray-sum`
  ↳ **Subarray Sum Equals K ✅** (#2, prefix sum + hashmap of seen sums — LADDER 2 COMPLETE)

### Ladder 3 — Kadane / Max Subarray  (GAP → high value) *(complete)*
`Maximum Subarray (plain Kadane) 🔁`
  ↳ **Maximum Sum Circular Subarray 🔁** (#10, Kadane twice: normal max + wrap-around)

### Ladder 4 — Sliding Window
`Longest Substring 🔁` → `Char Replacement ✅`
  ↳ **Continuous Subarrays ⬜** (#9, window + monotonic deque)

### Ladder 5 — Two-Pointer / Sort
`Two Sum II ✅` → `Valid Palindrome 🔁`
  ↳ **3Sum ✅** (#3) — already climbed

### Ladder 6 — Stack
`Valid Parens ✅` → `Daily Temperatures ✅ (monotonic)`
  ↳ **Largest Rectangle ✅** (#12) — already climbed

### Ladder 7 — Heap / heapq  (new territory)
`(new) heapq basics` → `Top K Frequent ✅ (heap variant)`
  ↳ **Reorganize String ⬜** (#14, heap + greedy)
  ↳ **Find K Pairs with Smallest Sums ⬜** (#19, heap)

### Ladder 8 — Trees  (new; keep basic)
`Max Depth 🔁` → `(new) tree traversal (DFS + BFS/level-order) ⬜`
  ↳ **Diameter of Binary Tree ⬜** (#4, easy, DFS returning height)
  ↳ **Binary Tree Vertical Order Traversal ⬜** (#16, BFS + column map)

### Ladder 9 — Graph / Grid  (new; worth 2-3)
`(new) Number of Islands ⬜ (DFS/BFS grid)`
  ↳ **Number of Distinct Islands ⬜** (#15)
  ↳ **Accounts Merge ⬜** (#6, union-find or DFS on graph)

### Ladder 10 — Backtracking  (lowest priority; only if time)
`(new) Subsets ⬜` → **Combination Sum II ⬜** (#20)

---

## 16-Day Schedule (foundation-first, ROI-ordered)

| Days | Ladders | Why |
|---|---|---|
| **1-2** | Ladder 1 (Hash Map targets) | foundation done → 3 fast wins, build confidence |
| **3-4** | Ladder 2 (Prefix Sum) + Ladder 3 (Kadane) | fills your 2 gaps + both are top-10 asked |
| **5** | Ladder 4 (redo Longest Substring, then Continuous Subarrays) | sliding-window refresh |
| **6-8** | Ladder 8 (Trees: Max Depth → traversal → Diameter → Vertical Order) | new territory, needs the most ramp |
| **9-10** | Ladder 7 (Heap: heapq → Reorganize → K Pairs) | new stdlib tool |
| **11-12** | Ladder 9 (Graph: Islands → Distinct Islands → Accounts Merge) | new territory |
| **13** | Cold-redo weak spots (bucket sort, Min Window, anything 🔁) | lock the shaky ones |
| **14-15** | Full narrated MOCKS — cold, timed, camera on | interview sim |
| **16** | Light review + rest. Interview. |

**Rule:** if a foundation rung feels shaky, redo IT before climbing to the target. Foundation solid = target is easy.

## The Tiers (practice top-down; master Tier 1 before touching Tier 3)

### 🥇 TIER 1 — ~70% of what you'll see. MASTER THESE.
Hash maps + arrays + strings + sliding window. Get them automatic + narrated.
- [x] Two Sum (hash map)
- [x] Valid Anagram / Group Anagrams (hash map keys)
- [x] Contains Duplicate / frequency counting
- [x] Top K Frequent (Counter + bucket)
- [ ] First Non-Repeating Character (hash map) ← new, very common
- [ ] Longest Substring Without Repeating Characters (sliding window)  ← TIER 1
- [ ] Longest Repeating Character Replacement (sliding window)
- [ ] Valid Palindrome / two-pointer string
- [ ] Best Time to Buy/Sell Stock (one-pass)

### 🥈 TIER 2 — common, has gaps to fill.
- [ ] Valid Parentheses (stack)
- [ ] Min Stack
- [ ] Evaluate RPN (stack)
- [ ] Prefix Sums — running total / subarray sum (⚠️ gap — Codility signature)
- [ ] Counting Elements / frequency-array tricks (⚠️ gap)
- [ ] Greedy — jump game / interval-style (⚠️ gap)
- [ ] Kadane's / Maximum Subarray (⚠️ gap — max-slice classic)

### 🥉 TIER 3 — nice to have, lower live-round frequency.
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Linked List Cycle (Floyd's)
- [ ] Binary Search (classic)
- [ ] Search in Rotated Sorted Array
- [ ] Tree traversal (in-order / level-order)
- [ ] Max Depth of Binary Tree / Invert Tree

### ⛔ SKIP — not a Toptal live-round thing
Hard DP, graphs, advanced trees, backtracking, N-Queens, etc.

---

## 17-Day Schedule (today = Day 0, evening)

| Days | Focus |
|---|---|
| **1-6** | TIER 1 cold-redo — narrated, timed, no old solutions. Repeat any that feel effortful. |
| **7-9** | TIER 2 — stacks redo + fill gaps (prefix sums, counting, greedy, Kadane) |
| **10-12** | TIER 3 — Linked Lists + Binary Search |
| **13-14** | TIER 3 — basic Trees + review weak spots |
| **15-17** | Full narrated MOCKS — cold, timed, camera-on, like the real Zoom |
| **18** | Light review + rest. Interview 5:45pm. |

---

## Every-problem ritual (this is the actual skill being tested)
1. **Restate** the problem in your own words + confirm with "interviewer"
2. **Clarify** edge cases / constraints out loud (empty input? dupes? negatives?)
3. **Brute force first**, state its Big-O, then say "we can do better"
4. **Optimized approach out loud** BEFORE typing
5. **Narrate while coding** — say what each line does as you write
6. **State time + space complexity**
7. **Test your own code** on an example + an edge case, out loud

I grade your **explanation**, not just whether it runs. Silent-but-correct = fail here.

Drills live in `toptal_drill/` — one `.py` per problem, Python only.
