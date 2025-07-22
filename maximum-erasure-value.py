from collections import defaultdict


def maximumUniqueSubarray():
    nums = [5,2,1,2,5,2,1,2,5] #8
    # res = sum(set(nums))

    n = len(nums)
    left = 0
    total = 0
    res = 0
    map = defaultdict(int)

    for i in range(n):
        map[nums[i]] += 1
        total += nums[i]
        while left < i and map[nums[i]] > 1:
            map[nums[left]] -= 1
            total -= nums[left]
            left += 1

        res = max(res, total)
            
        
    return res

print(maximumUniqueSubarray())