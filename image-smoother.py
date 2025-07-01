def imageSmoother():
    img = [[1,1,1],[1,0,1],[1,1,1]]

    ROWS = len(img)
    COLS = len(img[0])

    res = [[0] * COLS for _ in range(ROWS)]

    for r in range(ROWS):
        for c in range(COLS):
            count = 0
            total = 0

            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                        continue
                    count += 1
                    total += img[i][j]


            res[r][c] = total // count



    return res

print(imageSmoother())