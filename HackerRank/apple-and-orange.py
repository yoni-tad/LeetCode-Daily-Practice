def countApplesAndOranges():
    s = 7
    t = 11
    a = 4
    b = 12
    apples = [2, 3, -4]
    oranges = [3, -2, -4]
    # 1, 2

    tot_app = 0
    for i in apples:
        sum_app = i + a
        if sum_app >= s and sum_app <= t: 
            tot_app += 1
   
    tot_org = 0
    for j in oranges:
        sum_org = j + b
        if sum_org >= s and sum_org <= t: 
            tot_org += 1

    return [tot_app, tot_org]


print(countApplesAndOranges())

