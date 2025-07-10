import sys

def formingMagicSquare():
    s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]
    s = sum(s, [])

    magic = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 3, 8, 9, 5, 1, 2, 7, 6], [2, 7, 6, 9, 5, 1, 4, 3, 8],  [2, 9, 4, 7, 5, 3, 6, 1, 8], [4, 9, 2, 3, 5, 7, 8, 1, 6], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2]]

    cost = sys.maxsize

    for i in magic:
        diff = 0
        for j, k in zip(s, i):
            diff += abs(j - k)
        cost = min(cost, diff)
    return cost

print(formingMagicSquare())