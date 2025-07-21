def makeFancyString():
    s = "aaabaaaa" #"leetcode"
    n = len(s)

    if n <= 2: return s
    res = [s[0], s[1]]

    for i in range(2, n):
        if s[i] == s[i - 1] and s[i] == s[i - 2]: continue
        res.append(s[i])


    return "".join(res)

print(makeFancyString())