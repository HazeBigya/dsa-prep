from collections import deque


def continuousSubarrays(nums):
    maxDq = deque()
    minDq = deque()
    L = 0
    count = 0

    for R in range(len(nums)):
        while maxDq and nums[maxDq[-1]] < nums[R]:
            maxDq.pop()
        maxDq.append(R)

        while minDq and nums[minDq[-1]] > nums[R]:
            minDq.pop()
        minDq.append(R)

        while nums[maxDq[0]] - nums[minDq[0]] > 2:
            L += 1
            if maxDq[0] < L:
                maxDq.popleft()
            if minDq[0] < L:
                minDq.popleft()

        count += R - L + 1

    return count


if __name__ == "__main__":
    tests = [
        # (nums, expected)
        ([5, 4, 2, 4], 8),  # LeetCode sample
        ([1, 2, 3], 6),  # all subarrays valid
        ([1], 1),  # single element
        ([1, 1, 1, 1], 10),  # all equal -> n*(n+1)/2
        ([1, 4, 7, 10], 4),  # gaps too big -> only singles
        ([10, 8, 6, 4, 2], 9),  # singles + adjacent pairs (gap 2)
    ]

    failed = 0
    for nums, expected in tests:
        got = continuousSubarrays(list(nums))
        ok = got == expected
        failed += not ok
        print(f"{'PASS' if ok else 'FAIL'}  nums={nums} expected={expected} got={got}")

    print()
    print("ALL PASS" if failed == 0 else f"{failed} FAILED")
