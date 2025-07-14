def getDecimalValue():
    head = [1,0,1] #5

    arr = []
    current = head 
    while current is not None:
        arr.append(current.val)
        current = current.next
    return int(''.join(map(str, arr)), 2)


print(getDecimalValue())