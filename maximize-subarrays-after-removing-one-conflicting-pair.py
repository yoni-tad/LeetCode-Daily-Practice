from collections import defaultdict


def maxSubarrays():
    n = 4
    conflictingPairs = [[2,3],[1,4]] #9
    
    limits = defaultdict(list)
    for a, b in conflictingPairs:
        limits[max(a, b)].append((min(a, b)))
        
    res = 0
    left = [0, 0]
    an = [0] * (n + 1)
    for r in range(1, n + 1):
        for l in limits[r]:
            left = max(left, [left[0], l], [l, left[0]])
        res += r - left[0]
        an[left[0]] += left[0] - left[1]
             
    
    return res + max(an)

print(maxSubarrays())