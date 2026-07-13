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

| Problem | TS | Python | Pattern | Time | Space |
|---------|----|--------|---------|------|-------|
| [Two Sum](./two_sum) | ✅ | ✅ | Hash map (value → index) | O(n) | O(n) |
| [Contains Duplicate](./contains_duplicate) | ✅ | ✅ | Set membership | O(n) | O(n) |

## Structure

```
<problem_name>/
  <problem_name>.ts     # TypeScript solution
  <problem_name>.py     # Python solution
```

## Running

```bash
# TypeScript
npx tsx two_sum/two_sum.ts

# Python
python3 two_sum/two_sum.py
```
