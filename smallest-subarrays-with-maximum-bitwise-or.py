def smallestSubarrays():
    nums = [1,2]
    
    n = len(nums)
    last = [0] * 32
    res = [0] * n
    
    for i in range(n - 1, -1, -1):
        for bit in range(32):
            if nums[i] & (1 << bit):
                last[bit] = i
                
        res[i] = max(1, max(last) - i + 1)
        
    
    return res

print(smallestSubarrays())