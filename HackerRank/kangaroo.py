def kangaroo():
    x1 = 0
    v1 = 3
    x2 = 4
    v2 = 2

    if v1 > v2 and (x2 - x1) % (v1 - v2) == 0:
        return 'YES'
    return 'NO'

print(kangaroo())