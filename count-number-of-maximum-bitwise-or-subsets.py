def countMaxOrSubsets():
    nums = [2,2,2] #7

    mx = 0
    for x in nums: mx |= x

    self.res = 0

    def bt(start, curr):
        if curr == mx:
            self.res += 1
        
        for i in range(start, len(nums)):
            prev = curr
            curr |= nums[i]
            bt(i + 1, curr)
            curr = prev
    bt(0, 0)


    return self.res

print(countMaxOrSubsets())