def maxSum(nums):
    nums.sort()
    n = len(nums)
    if max(nums) < 0: return max(nums)
    if n == 1: return nums[0]

    sub = [nums[0]]
    tot = 0
    res = 0

    for i in range(0, n):
        if nums[i] < 0: continue
        if nums[i] <= sub[-1]: continue
        else:
            sub.append(nums[i])
            tot += nums[i]
        print(nums[i])
        print(sub)
    res = max(res, tot, sum(sub))

    return res


nums = [1,2,3,4,5] #15
# nums = [-20, 20] #20
# nums = [1,1,0,1,1] #1
print(maxSum([4,3,4,8]))