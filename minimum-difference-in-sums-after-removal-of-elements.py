import heapq


def minimumDifference():
    nums = [7,9,5,8,1,3] #1
    n = len(nums) // 3

    total_1 = sum(nums[:n])
    max_pq = [-x for x in nums[:n]]
    heapq.heapify(max_pq)

    part_1 = [0] * len(nums)
    part_1[n - 1] = total_1

    for i in range(n, n * 2):
        total_1 += nums[i]
        heapq.heappush(max_pq, -nums[i])
        total_1 -= -heapq.heappop(max_pq)
        part_1[i] = total_1

    total_2 = sum(nums[-n:])
    min_pq = nums[-n:]
    heapq.heapify(min_pq)

    part_2 = [0] * len(nums)
    part_2[n * 2] = total_2

    for i in range(n * 2 - 1, n - 1, -1):
        total_2 += nums[i]
        heapq.heappush(min_pq, nums[i])
        total_2 -= heapq.heappop(min_pq)
        part_2[i] = total_2

    res = float('inf')
    for i in range(n - 1, n * 2):
        res = min(res, part_1[i] - part_2[i + 1])

    return res

print(minimumDifference())