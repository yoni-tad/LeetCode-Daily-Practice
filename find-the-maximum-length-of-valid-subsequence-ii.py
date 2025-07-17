from collections import defaultdict


def maximumLength():
    nums = [1, 4, 2, 3, 1, 4]
    k = 3

    res =  0
    for x in range(k):
        map = defaultdict(int)

        for i in nums:
            i %= k
            map[i] = map[(x - i) % k] + 1
            res = max(res, map[i])

    return res

print(maximumLength())