def maxFreeTime():
    eventTime = 21
    k = 2
    startTime = [18,20]
    endTime = [20,21] #18

    free_gap = [startTime[0]]

    for i in range(1, len(startTime)):
        free_gap.append(startTime[i] - endTime[i - 1])
    
    free_gap.append(eventTime - endTime[-1])

    print(free_gap)

    ans = 0
    sum = 0

    for i in range(len(free_gap)):
        sum += free_gap[i] - (free_gap[i - (k + 1)] if i >= k + 1 else 0)
        ans = max(ans, sum)

    return ans

print(maxFreeTime())