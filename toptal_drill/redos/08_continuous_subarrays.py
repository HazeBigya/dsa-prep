from collections import deque


def continuos_subarray(nums):
    maxDq = deque()
    minDq = deque()
    count = 0
    L = 0

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
