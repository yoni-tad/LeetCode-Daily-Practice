def countHillValley():
    nums = [2,4,1,1,6,5] #3
    
    my = [nums[0]]
    for i in nums:
        if i == my[-1]: continue
        my.append(i)
            
    
    res = 0
    
    for i in range(1, len(my) - 1):
        left = my[i - 1]
        right = my[i + 1]
        
        if my[i] > left and my[i] > right:
            res += 1
            
        if my[i] < left and my[i] < right:
            res += 1
    
    return res

print(countHillValley())