def maximumLength():
    nums = [1,2,3,4] #4
    # nums = [1,2,1,1,2,1,2] #6

    odd = 0
    even = 0
    odd_even = 0
    even_odd = 0

    even_q = 0
    odd_q = 1

    for i in nums:
        if i % 2 == 0: even += 1
        else: odd += 1

        if  i % 2 == odd_q:
            odd_even += 1
            odd_q ^= 1
        if i % 2 == even_q:
            even_odd += 1
            even_q ^= 1

    return max(odd, even, odd_even, even_odd)

print(maximumLength())