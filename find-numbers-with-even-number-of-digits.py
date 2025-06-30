def findEvens():
    nums = [12,345,2,6,7896]

    tot = 0
    for i in nums:
        if len(str(i)) % 2 == 0:
            tot += 1
    return tot

print(findEvens())