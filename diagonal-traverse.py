def findDiagonalOrder():
    mat = [[1,2,3],[4,5,6],[7,8,9]] #[1,2,4,7,5,3,6,8,9]

    '''
        1   2   3
        4   5   6
        7   8   9
    '''

    row = len(mat)
    col = len(mat[0])
    diagonals = [[] for _ in range(row + col - 1)]

    for i in range(row):
        for j in range(col):
            diagonals[i + j].append(mat[i][j])


    res = diagonals[0]
    for i in range(1, len(diagonals)):
        if i % 2 == 1:
            res.extend(diagonals[i])
        else:
            res.extend(diagonals[i][::-1]) 
    return res

print(findDiagonalOrder())