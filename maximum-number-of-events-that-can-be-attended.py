import heapq


def maxEvents():
    events = [[1,2],[1,2],[3,3],[1,5],[1,5]] #5
    events.sort()

    total = max(event[1] for event in events)

    min_heap = []
    n = len(events)
    i = 0
    day = 1
    count = 0

    while day <= total:
        if not min_heap and i < n:
            day = max(day, events[i][0])
        
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)
        
        while i < n and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])
            i += 1
        
        if min_heap:
            heapq.heappop(min_heap)
            count += 1
        elif i == n:
            break
            
        day += 1
        
    return count




    # events = [[1,2],[1,2],[1,5],[1,5], [3, 3]]
    # sorted_events = sorted(events, key=lambda x: (x[1], x[0]))

    # count = 0
    # for i in range(1, len(events) + 1):
    #     arr = []
    #     for j in sorted_events:
    #         if i >= j[0]:
    #             arr.append(j)
        
    #     sorted_arr = sorted(arr, key=lambda x: x[1])
    #     if sorted_arr[0][0] <= i <= sorted_arr[0][1]:
    #         count += 1
    #         sorted_events.remove(sorted_arr[0])


    # day = 1
    # count = 0
    # for i in sorted_events:
    #     if i[0] <= day <= i[1]:
    #         print(day)
    #         count += 1
    #     day += 1

    # print(sorted_events)
    # return count

print(maxEvents())