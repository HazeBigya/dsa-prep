def minZeroArray(nums, queries):
    lo = 0
    hi = len(queries)
    answer = -1

    def enough(nums, queries, k):
        n = len(nums)
        diff = [0] * (n + 1)
        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            diff[r + 1] -= val

        running = 0

        for i in range(n):
            running += diff[i]
            if running < nums[i]:
                return False
        return True

    while lo <= hi:
        mid = (lo + hi) // 2
        if enough(nums, queries, mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


if __name__ == "__main__":
    tests = [
        # (nums, queries, expected)
        ([2, 0, 2], [[0, 2, 1], [0, 2, 1], [1, 1, 3]], 2),  # LeetCode sample
        ([4, 3, 2, 1], [[1, 3, 2], [0, 2, 1]], -1),  # impossible
        ([0, 0, 0], [[0, 2, 5]], 0),  # already zero -> k=0
        ([1], [[0, 0, 1]], 1),  # single bucket
        ([5], [[0, 0, 2], [0, 0, 2], [0, 0, 2]], 3),  # needs all queries
        ([2, 2], [[0, 1, 1], [0, 1, 1]], 2),
        ([0], [], 0),  # no queries, already zero
        ([1], [], -1),  # no queries, impossible
        ([1, 2, 3, 4], [[0, 3, 1]] * 4, 4),
        ([3, 3, 3], [[0, 0, 3], [1, 1, 3], [2, 2, 3]], 3),  # each query hits one index
        (
            [1, 1, 1],
            [[2, 2, 1], [1, 1, 1], [0, 0, 1]],
            3,
        ),  # last query is the one needed
    ]

    failed = 0
    for nums, queries, expected in tests:
        got = minZeroArray(list(nums), queries)
        ok = got == expected
        failed += not ok
        print(
            f"{'PASS' if ok else 'FAIL'}  nums={nums} queries={queries} "
            f"expected={expected} got={got}"
        )

    print()
    print("ALL PASS" if failed == 0 else f"{failed} FAILED")
