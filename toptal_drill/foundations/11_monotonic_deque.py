"""
Foundation #11 — Monotonic Deque (window max / min in O(1))
Holds up: drill 08 (Continuous Subarrays)

WHY:
  Sliding window needs max(window) and min(window) every step.
  Rescanning the window each time = O(n^2). Too slow.
  A monotonic deque keeps the answer sitting at the FRONT, O(1).

THE ONE RULE (max-deque):
  New element x arrives. Pop from the BACK while back < x.
  Reason: that back element is SMALLER than x *and* leaves the window
  EARLIER than x -> it can never be the max again -> delete forever.
  (min-deque is the mirror: pop while back > x)

  Same "pop everything the new guy dominates" logic as the monotonic
  STACK from Daily Temperatures / Largest Rectangle. Cousin pattern.

WE STORE INDICES, NOT VALUES — so we can tell when the front has slid
out of the window (front <= r - k means it fell off the left edge).

Fill in every ___ blank, then run:  python3 11_monotonic_deque.py
"""

from collections import deque

# ---------------------------------------------------------------
# PART 1 — deque basics (a list you can push/pop from BOTH ends)
# ---------------------------------------------------------------
dq = deque()
dq.append(1)  # add to BACK    -> [1]
dq.append(2)  # add to BACK    -> [1, 2]
dq.appendleft(0)  # add to FRONT   -> [0, 1, 2]

print("PART 1 deque:", list(dq))  # expect [0, 1, 2]
print("PART 1 front:", dq[0])  # front  -> 0
print("PART 1 back: ", dq[-1])  # back   -> 2

dq.pop()  # remove from BACK  -> [0, 1]
dq.popleft()  # remove from FRONT -> [1]
print("PART 1 after pops:", list(dq))  # expect [1]


# ---------------------------------------------------------------
# PART 2 — sliding window MAXIMUM  (LeetCode 239)
# Fixed window of size k slides left to right. Report max each step.
#   nums = [1,3,-1,-3,5,3,6,7], k = 3  ->  [3,3,5,5,6,7]
# ---------------------------------------------------------------
def slidingWindowMax(nums, k):
    dq = deque()  # holds INDICES; their values stay DECREASING
    out = []

    for r in range(len(nums)):
        # 1) new guy dominates: pop weaker elements off the BACK
        while dq and nums[dq[-1]] < nums[r]:
            dq.pop()

        # 2) new guy joins the back
        dq.append(r)

        # 3) front fell out of the window? evict it
        #    window covers [r-k+1 .. r], so anything <= r-k is outside
        if dq[0] <= r - k:
            dq.popleft()

        # 4) once the window is full, record the max (which lives at...)
        if r >= k - 1:
            out.append(nums[dq[0]])

    return out


print("PART 2:", slidingWindowMax([1, 3, -1, -3, 5, 3, 6, 7], 3))
# expect [3, 3, 5, 5, 6, 7]


# ---------------------------------------------------------------
# PART 3 — sliding window MINIMUM  (exact mirror of Part 2)
# Only ONE character changes vs Part 2. Find it.
#   nums = [1,3,-1,-3,5,3,6,7], k = 3  ->  [-1,-3,-3,-3,3,3]
# ---------------------------------------------------------------
def slidingWindowMin(nums, k):
    dq = deque()  # holds INDICES; their values stay INCREASING
    out = []

    for r in range(len(nums)):
        while dq and nums[dq[-1]] > nums[r]:  # flip the comparison!
            dq.pop()
        dq.append(r)

        if dq[0] <= r - k:
            dq.popleft()

        if r >= k - 1:
            out.append(nums[dq[0]])

    return out


print("PART 3:", slidingWindowMin([1, 3, -1, -3, 5, 3, 6, 7], 3))
# expect [-1, -3, -3, -3, 3, 3]


# ---------------------------------------------------------------
# PART 4 — mini-drill: BOTH deques at once, track the GAP
# Window only GROWS here (no shrinking yet — that's drill 08's job).
# After each new element, report max - min of everything seen so far.
#   nums = [5,4,2,4]  ->  gaps [0, 1, 3, 3]
# ---------------------------------------------------------------
def runningGaps(nums):
    maxDq = deque()  # values DECREASING -> front = max
    minDq = deque()  # values INCREASING -> front = min
    gaps = []

    for r in range(len(nums)):
        while maxDq and nums[maxDq[-1]] < nums[r]:
            maxDq.pop()
        maxDq.append(r)

        while minDq and nums[minDq[-1]] > nums[r]:
            minDq.pop()
        minDq.append(r)

        window_max = nums[maxDq[0]]  # where does the answer live?
        window_min = nums[minDq[0]]
        gaps.append(window_max - window_min)

    return gaps


print("PART 4:", runningGaps([5, 4, 2, 4]))
# expect [0, 1, 3, 3]
#   [5]        max 5 min 5 -> 0
#   [5,4]      max 5 min 4 -> 1
#   [5,4,2]    max 5 min 2 -> 3
#   [5,4,2,4]  max 5 min 2 -> 3
