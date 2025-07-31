def subarrayBitwiseORs():
    arr = [1,1,2]
    
    
    curr = set()
    res = set()
    
    for x in arr:
        temp = set()
        for y in curr: temp.add(x | y)
        temp.add(x)
        curr = temp
        res |= curr
    
    return len(res)

print(subarrayBitwiseORs())