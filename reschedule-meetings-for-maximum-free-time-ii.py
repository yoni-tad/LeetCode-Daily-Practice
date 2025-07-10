def maxFreeTime():
    eventTime = 5
    startTime = [1,3]
    endTime = [2,5] #2
    n = len(startTime)

    space = [False] * n
    s_1 = 0

    for i in range(n):
        if endTime[i] - startTime[i] <= s_1: space[i] = True
        s_1 = max(s_1, startTime[i] - (0 if i == 0 else endTime[i - 1]))

    s_2 = 0
    for i in range(n - 1, -1, -1):
        if endTime[i] - startTime[i] <= s_2: space[i] = True
        s_2= max(s_2, (eventTime if i == n - 1 else startTime[i + 1]) - endTime[i])

    
    ans = 0
    for i in range(n):
        left = 0 if i == 0 else endTime[i - 1]
        right = eventTime if i == n - 1 else startTime[i + 1]

        if space[i]:
            ans = max(ans, right - left)
        else:
            ans = max(ans, right - left - (endTime[i] - startTime[i]))


    return ans

print(maxFreeTime())