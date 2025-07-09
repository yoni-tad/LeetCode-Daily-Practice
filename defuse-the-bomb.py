def decrypt():
    code = [2,4,9,3]
    k = -2 #[12,5,6,13]

    n = len(code)
    ans = [0] * n

    if k == 0:
        return ans
    
    if k > 0:
        s = sum(code[1: k + 1]) 
        for i in range(n):
            ans[i] = s
            s = s - code[(i + 1) % n] + code[(i + k + 1) % n]

    if k < 0:
        s = sum(code[k:])

        for i in range(n):
            ans[i] = s
            s = s + code[(i) % n] - code[(i + k) % n]


    return ans

print(decrypt())