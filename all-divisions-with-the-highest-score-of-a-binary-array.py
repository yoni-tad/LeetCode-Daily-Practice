def allDivisions():
    nums = [1,0,1,0,1,1,0,1,0] #[4,0,2]

    n = len(nums)
    left = 0
    right = sum(nums)
    ans = [0]
    max = sum(nums)

    for i in range(n):
        if nums[i] == 0:
            left += 1
        else:
            right -= 1
        
        total = left + right
        if max == total:
            ans.append(i + 1)
        elif max < total:
            ans = []
            ans.append(i + 1)
            max = total




    # My first attempt
    
    # res = []
    # for i in range(n + 1):
    #     num_left = 0
    #     num_right = 0
    #     if i == 0:
    #         num_right += nums[i:].count(1)
    #     elif i == n or i == n - 1:
    #         num_left += nums[:i].count(0)
    #     else:
    #         num_left += nums[:i].count(0)
    #         num_right += nums[i:].count(1)
        
    #     sum = num_left + num_right
    #     res.append([i, sum])
    
    # ans = []
    # maximum = max(res, key=lambda x:x[1])[1]  
    # for j in res:
    #     if maximum == j[1]:
    #         ans.append(j[0])

    return ans

print(allDivisions())