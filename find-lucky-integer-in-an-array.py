def findLucky():
    arr = [2,2,3,4] #2
    arr.sort(reverse=True)

    res = dict()
    for i in arr:
        if i in res:
            res[i] = res[i] + 1
        else:
            res[i] = 1

    for key, value in res.items():
        if key == value:
            return value 

    return -1

print(findLucky())