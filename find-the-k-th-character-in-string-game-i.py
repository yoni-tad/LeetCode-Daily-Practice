def kthCharacter():
    word = "a"
    k = 5
    # a = 97 and z = 122

    res = word
    count = len(res)

    while True:
        for i in res:
            res += chr(ord(i) + 1)

        count += 1
        if len(res) > k or count > k:
            break

    print(res[k - 1])

    return True

print(kthCharacter())