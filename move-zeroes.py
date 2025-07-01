def moveZeroes():
    nums = [0,1,0,3,12]  #[1,3,12,0,0]
    write = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[i]
            nums[i] = nums[write]
            nums[write] = temp
            write += 1
    return nums

print(moveZeroes())