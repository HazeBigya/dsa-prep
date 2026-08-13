"""
Foundation #10 — Difference Array (range updates in O(1))
Holds up: drill 07 (Zero Array Transformation II)

IDEA:
  To add `v` to every element in range [l, r]:
      diff[l]   += v      # turn ON +v starting at l
      diff[r+1] -= v      # turn it back OFF right after r
  Then PREFIX SUM over diff reconstructs the real values.
  Each update touches only 2 cells -> O(1) per range update.

Fill in every ___ blank, then run:  python3 10_difference_array.py
"""

# ---------------------------------------------------------------
# PART 1 — one range update by hand
# nums length 5, all zeros. Apply: add 3 to [1..3].
# ---------------------------------------------------------------
n = 5
diff = [0] * (n + 1)  # +1 slot so r+1 never goes out of bounds

l, r, v = 1, 3, 3
diff[l] += v  # turn on
diff[r + 1] -= v  # turn off just after r

# rebuild real values with a running prefix sum
result = []
running = 0
for i in range(n):
    running += diff[i]
    result.append(running)

print("PART 1:", result)  # expect [0, 3, 3, 3, 0]


# ---------------------------------------------------------------
# PART 2 — stack MULTIPLE range updates, THEN one prefix pass
# nums length 5, all zeros.
#   add 3 to [1..3]
#   add 5 to [0..2]
#   add 2 to [2..4]
# ---------------------------------------------------------------
n = 5
diff = [0] * (n + 1)

updates = [(1, 3, 3), (0, 2, 5), (2, 4, 2)]
for l, r, v in updates:
    diff[l] += v
    diff[r + 1] -= v  # same off-switch position

result = []
running = 0
for i in range(n):
    running += diff[i]  # accumulate the deltas
    result.append(running)

print("PART 2:", result)  # expect [5, 8, 10, 5, 2]


# ---------------------------------------------------------------
# PART 3 — mini-drill: coverage / capacity
# Each query says "this index gets up to `v` decrement capacity".
# Question: after ALL queries, how much total capacity does each index have?
# (This is EXACTLY what drill 07 needs.)
#   queries = [l, r, val]
# ---------------------------------------------------------------
def coverage(n, queries):
    diff = [0] * (n + 1)
    for l, r, val in queries:
        diff[l] += val
        diff[r + 1] -= val  # off-switch
    cap = []
    running = 0
    for i in range(n):
        running += diff[i]
        cap.append(running)  # what do we append? the running total
    return cap


print("PART 3:", coverage(3, [[0, 2, 1], [0, 2, 1], [1, 1, 3]]))
# expect [2, 5, 2]  (idx0: 1+1, idx1: 1+1+3, idx2: 1+1)
