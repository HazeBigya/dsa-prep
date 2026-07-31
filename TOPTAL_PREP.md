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

## The Tiers (practice top-down; master Tier 1 before touching Tier 3)

### 🥇 TIER 1 — ~70% of what you'll see. MASTER THESE.
Hash maps + arrays + strings + sliding window. Get them automatic + narrated.
- [ ] Two Sum (hash map)
- [ ] Valid Anagram / Group Anagrams (hash map keys)
- [ ] Contains Duplicate / frequency counting
- [ ] Top K Frequent (Counter + bucket)
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
