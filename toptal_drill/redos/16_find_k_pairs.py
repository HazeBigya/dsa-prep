"""
Toptal Target #16 — Find K Pairs with Smallest Sums
Difficulty: Medium  |  Pattern: min-heap (k-way merge frontier)

WORKED SOLUTION + derivation (study, don't memorize).

=============================================================================
THE QUESTION
=============================================================================
Two SORTED arrays nums1, nums2 and an int k.
A "pair" is one number from each: (nums1[i], nums2[j]).
Return the k pairs with the smallest SUM a+b.

    nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    all pair sums:
        1+2=3   1+4=5   1+6=7
        7+2=9   7+4=11  7+6=13
        11+2=13 11+4=15 11+6=17
    3 smallest -> [1,2],[1,4],[1,6]

=============================================================================
HOW THE SOLUTION IS DERIVED
=============================================================================
Brute force: build ALL n*m pair sums, sort, take k.
    time O(n*m log(n*m)). Wasteful — we only want k, not all n*m.

Key observation (this is the whole trick):
  Because both arrays are SORTED, the very smallest pair is always
  (nums1[0], nums2[0]).  And once you've picked pair (i, j), the NEXT
  candidates that could be smallest are its two neighbors:
        (i+1, j)   -- step down nums1
        (i,   j+1) -- step right nums2
  So the pairs form a grid, and the smallest sums spread out from the
  top-left corner like a wavefront. We never need the far corner.

That "always grab the current smallest, then expose its neighbors" is
exactly what a MIN-HEAP does. Heap = the frontier of candidates we've
uncovered but not yet chosen.

To avoid pushing the same (i,j) twice from two directions, use ONE clean
seeding rule instead of both neighbors:
  - Seed the heap with (nums1[i] + nums2[0], i, 0) for each row i
    (capped at k rows — more than k rows can never contribute to k answers).
  - Every time we pop (sum, i, j), the only new cell to expose is (i, j+1)
    -- the next column in the SAME row. Each row advances left->right
    independently, so no cell is ever reached twice. No visited-set needed.

This is the classic "k-way merge": treat each row of nums1 as a sorted
list (nums1[i]+nums2[0], +nums2[1], ...) and merge them by smallest front.

=============================================================================
BIG-O
=============================================================================
Let K = number of pairs we return (min(k, n*m)).
  - Seeding: up to min(k, n) pushes             -> O(k log k)
  - Then K iterations, each 1 pop + <=1 push    -> O(k log k)
  Time  : O(k log k)
  Space : O(k)  -- heap holds at most ~k entries (the output is excluded
                   by convention; if counted it's also O(k)).
Beats brute force's O(n*m log(n*m)) whenever k << n*m.
"""

import heapq


def kSmallestPairs(nums1, nums2, k):
    # Edge: either array empty, or k is 0 -> no pairs possible.
    if not nums1 or not nums2 or k == 0:
        return []

    result = []
    heap = []

    # SEED: pair each of the first k rows with column 0.
    # We only need the first min(k, len(nums1)) rows because the answer has
    # at most k pairs, and each row can contribute at most one pair before
    # any other row's second pair would be needed.
    for i in range(min(k, len(nums1))):
        # store (sum, i, j). sum is first so the heap orders by it.
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    # Pull the smallest sum k times.
    while heap and len(result) < k:
        _, i, j = heapq.heappop(heap)          # current smallest pair
        result.append([nums1[i], nums2[j]])

        # Expose the next column in THIS row: (i, j+1).
        # Only push if that column exists.
        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result


# --------------------------------------------------------------------------
# self-tests
# --------------------------------------------------------------------------
if __name__ == "__main__":
    def check(got, exp):
        print("PASS" if got == exp else "FAIL", "got", got, "exp", exp)

    check(kSmallestPairs([1, 7, 11], [2, 4, 6], 3), [[1, 2], [1, 4], [1, 6]])
    check(kSmallestPairs([1, 1, 2], [1, 2, 3], 2), [[1, 1], [1, 1]])
    check(kSmallestPairs([1, 2], [3], 3), [[1, 3], [2, 3]])   # k > total pairs
    check(kSmallestPairs([], [1, 2], 3), [])                  # empty input
    check(kSmallestPairs([1, 2], [3], 0), [])                 # k == 0
