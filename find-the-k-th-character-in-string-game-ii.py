def kthCharacter():
    k = 10
    operations = [0,1,0,1] # "b"

    k -= 1
    res = 0

    for i in range(min(len(operations), 60)):
        if (k >> i) & 1:
            res += operations[i]

    return chr((res % 26) + ord('a'))


print(kthCharacter())