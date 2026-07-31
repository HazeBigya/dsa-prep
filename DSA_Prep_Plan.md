# DSA Prep Plan — For an Experienced Engineer (Big Tech / AI Labs)

**Goal:** Make Mediums effortless, execute clean and fast under pressure, and communicate while coding. You already have the engineering judgment — this is about pattern fluency and interview execution, not learning to code.

**Target:** ~8 weeks at a sustainable pace. Adjust freely; consistency beats intensity.

**Core principle:** Study by *pattern*, not randomly. Do a batch of the same pattern until it clicks, then move on. Aim for **~2 problems/day on weekdays**, lighter or review on weekends. That's ~10–12/week, ~80–100 total — enough for someone with your experience.

**Primary resource:** NeetCode 150 (organized by pattern) or Grind 75. Use LeetCode for the problems themselves.

---

## How to practice each problem (the method matters more than the count)

- [ ] Read the problem, restate it in your own words out loud
- [ ] Talk through your approach BEFORE coding (this is what interviews test)
- [ ] Code it cleanly, narrating your thinking
- [ ] State time & space complexity out loud
- [ ] If stuck >25–30 min, read the solution, understand the pattern, then redo it from scratch later
- [ ] Once a week: redo 2–3 older problems cold (spaced repetition)

**Rule:** A problem you solved by reading the answer is NOT done until you can solve it cold days later.

---

## Fundamentals — Warmups

Not NeetCode 150, but frequent phone-screen / warmup questions. Build syntax fluency and loop/recursion reflexes before the pattern work. In `fundamentals/`.

- [x] Fibonacci (iterative — series + nth value)
- [x] Prime number check (√n bound)
- [x] Factorial (iterative + recursive)
- [x] Sort an array (built-in + one manual, e.g. bubble/insertion)
- [x] Reverse sort (descending)
- [x] Reverse a string
- [x] Reverse an array/list in place
- [x] FizzBuzz
- [x] Sum / count of digits
- [x] Palindrome number (integer, no string convert)
- [x] GCD / LCM (Euclid's algorithm)
- [x] Max / min in an array (single pass)

---

## Week 1 — Arrays, Hashing, Two Pointers

Foundation patterns. These show up constantly and build momentum.

- [x] Two Sum
- [x] Contains Duplicate
- [x] Valid Anagram
- [x] Group Anagrams
- [x] Top K Frequent Elements
- [x] Product of Array Except Self
- [x] Valid Palindrome
- [x] Two Sum II (sorted)
- [x] 3Sum
- [x] Container With Most Water

---

## Week 2 — Sliding Window & Stack

High-frequency patterns; sliding window trips up many people, so drill it.

- [x] Best Time to Buy/Sell Stock
- [x] Longest Substring Without Repeating Characters
- [x] Longest Repeating Character Replacement
- [x] Minimum Window Substring (hard — attempt, learn the pattern)
- [x] Valid Parentheses
- [x] Min Stack
- [x] Evaluate Reverse Polish Notation
- [x] Daily Temperatures
- [x] Car Fleet
- [x] Largest Rectangle in Histogram (hard — pattern exposure)

---

## Week 3 — Binary Search & Linked Lists

- [ ] Binary Search
- [ ] Search a 2D Matrix
- [ ] Koko Eating Bananas
- [ ] Find Minimum in Rotated Sorted Array
- [ ] Search in Rotated Sorted Array
- [ ] Reverse Linked List
- [ ] Merge Two Sorted Lists
- [ ] Reorder List
- [ ] Remove Nth Node From End
- [ ] Linked List Cycle
- [ ] Add Two Numbers

---

## Week 4 — Trees (the big one)

Trees are interview bread-and-butter. Spend extra time here.

- [ ] Invert Binary Tree
- [ ] Maximum Depth of Binary Tree
- [ ] Diameter of Binary Tree
- [ ] Balanced Binary Tree
- [ ] Same Tree
- [ ] Subtree of Another Tree
- [ ] Lowest Common Ancestor of a BST
- [ ] Binary Tree Level Order Traversal
- [ ] Validate Binary Search Tree
- [ ] Kth Smallest Element in a BST
- [ ] Construct Tree from Preorder and Inorder

---

## Week 5 — Tries, Heaps / Priority Queue, Backtracking

- [ ] Implement Trie (Prefix Tree)
- [ ] Design Add and Search Words Data Structure
- [ ] Kth Largest Element in a Stream
- [ ] Last Stone Weight
- [ ] K Closest Points to Origin
- [ ] Task Scheduler
- [ ] Subsets
- [ ] Combination Sum
- [ ] Permutations
- [ ] Word Search

---

## Week 6 — Graphs (critical for system-y roles)

Your backend/cloud background makes graph intuition natural — lean in.

- [ ] Number of Islands
- [ ] Clone Graph
- [ ] Pacific Atlantic Water Flow
- [ ] Course Schedule (topological sort)
- [ ] Course Schedule II
- [ ] Graph Valid Tree
- [ ] Number of Connected Components
- [ ] Rotting Oranges
- [ ] Walls and Gates
- [ ] Word Ladder (hard — pattern exposure)

---

## Week 7 — Dynamic Programming (1D + intro 2D)

The scariest for most; the trick is recognizing overlapping subproblems. Don't aim to master every DP — aim to recognize the common shapes.

- [ ] Climbing Stairs
- [ ] Min Cost Climbing Stairs
- [ ] House Robber
- [ ] House Robber II
- [ ] Longest Palindromic Substring
- [ ] Palindromic Substrings
- [ ] Decode Ways
- [ ] Coin Change
- [ ] Maximum Product Subarray
- [ ] Longest Increasing Subsequence
- [ ] Unique Paths (2D)
- [ ] Longest Common Subsequence (2D)

---

## Week 8 — Greedy, Intervals, Mixed Review + Mock Interviews

- [ ] Maximum Subarray (Kadane's)
- [ ] Jump Game
- [ ] Insert Interval
- [ ] Merge Intervals
- [ ] Non-overlapping Intervals
- [ ] Meeting Rooms / Meeting Rooms II
- [ ] **Do 3–4 full mock interviews** (Pramp, interviewing.io, or a friend) — timed, out loud, one problem each
- [ ] Redo 10 older problems cold to lock in retention

---

## System Design Track — CO-EQUAL with DSA (not a side track)

**Reprioritized 2026-07-28 after a real interview.** The wobble wasn't a LeetCode miss — it was system design + explaining-your-own-reasoning under pressure. For the roles targeted (Big Tech / AI Labs, senior/experienced), that articulation gap is the *higher-leverage* fix right now. So this is co-equal with the DSA weeks — give it equal time, not leftover time.

**One design per week**, ~60–90 min: sketch it, talk it out loud, write the tradeoffs. This is where your production/backend/cloud experience shines — lean in. Laddered easy→hard, ending on your AI/RAG edge.

**The core drill (do this every design, out loud): "Why THIS and not the obvious alternative?"** For every choice, name the alternative and defend against it. NoSQL — why not SQL? Cache-aside — why not write-through? Optimistic lock — why not pessimistic? This exact move — justifying a choice against its alternative on the spot — is what scattered under pressure today. Rehearse it until it's automatic. A design isn't done until you can defend every box against the thing you *didn't* pick.

**Method for every design (same each time):**
1. **Clarify requirements** — functional + non-functional (scale, latency, consistency vs availability). Ask questions, don't assume.
2. **Back-of-envelope estimates** — QPS, storage, bandwidth. Order of magnitude.
3. **API design** — the key endpoints/contracts.
4. **Data model** — schema, SQL vs NoSQL and *why*.
5. **High-level diagram** — boxes + arrows, request flow.
6. **Deep-dive** — 1–2 components the interviewer probes (the interesting part).
7. **Bottlenecks & tradeoffs** — what breaks at scale, how you'd fix (cache, shard, replicate, queue), CAP choices.

- [ ] Wk1 — **URL Shortener (TinyURL)** — hashing/base62, KV store, read-heavy cache, redirect flow
- [ ] Wk2 — **Rate Limiter** — token bucket vs sliding window, where it lives, distributed counter (Redis)
- [ ] Wk3 — **Pastebin / Image Host** — blob storage (S3), CDN, metadata DB, TTL/expiry
- [ ] Wk4 — **Web Crawler** — BFS at scale, URL dedup (bloom filter), politeness, distributed workers + queue
- [ ] Wk5 — **Chat / Messaging (WhatsApp)** — websockets, presence, message fanout, delivery guarantees, queues
- [ ] Wk6 — **News Feed (Twitter/Instagram)** — fanout-on-write vs on-read, timeline cache, celebrity problem
- [ ] Wk7 — **Video Streaming (YouTube/Netflix)** — upload+transcode pipeline, CDN, adaptive bitrate, storage tiers
- [ ] Wk7 — **Ticketing System (50k seats, 500k concurrent users)** — THE concurrency problem. Seat locking (optimistic vs pessimistic), preventing overselling, reservation hold + TTL, virtual waiting room / queue (Ticketmaster-style), idempotent booking, DB row-lock vs Redis lock, payment saga. Deep-dive the race condition: two users, one seat.
- [ ] Wk8 — **RAG / LLM Serving System** (your edge) — vector DB, embedding pipeline, retrieval + rerank, chunking, caching, latency/cost tradeoffs, eval

*(Wk7 has two designs — Video Streaming + Ticketing. Do Ticketing if you only have time for one; the concurrency deep-dive is higher-signal for most interviews.)*

### Low-Level / OOD Design (separate interview format)

Some rounds want **object-oriented design** — classes, interfaces, state machines, design patterns — not distributed boxes-and-arrows. Whiteboard the class diagram + key methods.

- [ ] **Elevator System** — `Elevator`, `Floor`, `Request`, `Scheduler`. State machine (idle/up/down/maintenance). Scheduling algo (SCAN/LOOK vs naive FCFS). Multi-elevator dispatch. Thread-safety of the request queue. This is a state-machine + strategy-pattern problem, not a QPS/sharding one.
- [ ] **Parking Lot**, **Vending Machine**, **Chess/Tic-Tac-Toe** — other common LLD warmups if asked.

**Resources:** *System Design Interview* (Alex Xu vol 1+2), ByteByteGo, the Grokking course. For LLD: *Head First Design Patterns*, refactoring.guru. But don't just read — *produce* a design each week, out loud.

## Ongoing habits (keep after week 8)

- [ ] 1–2 problems/day maintenance so skills don't decay
- [ ] Weekly: one timed mock, out loud
- [ ] Keep a "mistakes log" — patterns you keep missing; review before interviews
- [ ] **Vocabulary map** ([VOCAB_MAP.md](./VOCAB_MAP.md)) — running two-column doc: LEFT = how you describe your real work in plain words, RIGHT = the textbook term. Your recurring gap is *knowing the thing but not the formal word* (e.g. "status change so first wins" → optimistic locking / atomic conditional write). Add a row every time it happens. Review before every interview. Highest ROI habit — an afternoon of work, not eight weeks.
- [ ] Balance with **system design** prep (separate track) and your **AI/RAG depth** (your edge)

---

## Balance reminder

DSA is one leg of three. Don't over-invest here at the expense of:
1. **System design** — where your real production experience shines (elevator, URL shortener, rate limiter, news feed, chat system, etc.)
2. **AI/RAG depth** — your differentiator for AI-lab roles; be ready to go deep on what you actually built
3. **Behavioral** — leadership stories, tradeoffs, conflicts, impact

A sustainable pace you actually keep beats a burnout sprint you abandon in week 2. Consistency wins this.
