def zero_array_transformation(nums, queries):
    lo = 0
    hi = len(queries)
    answer = -1

    while lo <= hi:
        mid = (lo + hi) // 2
        if check(nums, queries, mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer


def check(nums, queries, k):
    n = len(nums)
    diff = [0] * (n + 1)

    for i in range(k):
        L, R, val = queries[i]
        diff[L] += val
        diff[R + 1] -= val

    running = 0

    for i in range(n):
        running += diff[i]
        if running < nums[i]:
            return False
    return True


nums = [2, 0, 2]
queries = [[0, 2, 1], [0, 2, 1], [1, 1, 3]]
print(zero_array_transformation(nums, queries))
