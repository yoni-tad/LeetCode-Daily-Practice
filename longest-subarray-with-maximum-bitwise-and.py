def longestSubarray():
    nums = [1,2,3,3,2,2]
    
    n = len(nums)
    mx = max(nums)
    curr = 0
    res = 0
    
    for i in range(n):
        if nums[i] == mx: curr += 1
        else: curr = 0
        res = max(res, curr)
            
    return res

print(longestSubarray())