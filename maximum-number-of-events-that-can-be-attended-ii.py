from bisect import bisect_right
from functools import lru_cache


def maxValue():
    events = [[1,2,4],[3,4,3],[2,3,10]]
    k = 2 #10
    events.sort()
    n = len(events)
    start_days = [e[0] for e in events]

    @lru_cache(None)
    def dp(i, remaining):
        if i == n or remaining == 0:
            return 0
        
        reject = dp(i + 1, remaining)
        next_i = bisect_right(start_days, events[i][1])
        select = events[i][2] + dp(next_i, remaining - 1)

        return max(reject, select)
        
    return dp(0, k)
















    # dp = [[0] * (k + 1) for _ in range(n)]

    # events.sort(key= lambda x: x[0])

    # def helper(events, position, k, n):
    #     if position >= n or k == 0:
    #         return 0

    #     if dp[position][k] > 0:
    #         return dp[position][k]

    #     next_event = nextEvent(events, position, n)
    #     select = events[position][2] + helper(events, next_event, k, n)
    #     reject = helper(events, position + 1, k, n)
    #     dp[position][k] = max(select, reject)
    #     return dp[position][k]


    # def nextEvent(events, position, n):
    #     last_day = events[position][1]
    #     position += 1

    #     while position < n:
    #         mid = position + (n - position) // 2

    #         if events[mid][0] > last_day:
    #             n = mid
    #         else:
    #             position += 1
    #     return n

    # return helper(events, 0, k, n)








    # events = [[1,2,4],[3,4,3],[2,3,10]]
    # k = 2 #10

    
    # n = len(events)

    # print(events)

    # ans = events[0][2]
    # for i in range(len(events[1:])):
    #     for j in range(i + 1, len(events[1:])):
    #         if events[i][0] not in events[j][0:2] and events[i][1] not in events[j][0:2]:
    #             print(events[i])
    #             ans += events[i][2]
    

print(maxValue())