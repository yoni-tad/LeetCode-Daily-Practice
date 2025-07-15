def climbingLeaderboard():
    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # player = [5, 25, 50, 120]

    ranked = [100, 90, 90, 80]
    player = [70, 80, 105] #[4, 3, 1]

    ans = []

    a = {}
    rank = 1
    for i in sorted(ranked + player, reverse=True):
        if i not in a:
            a[i] = rank
            rank += 1
        

    for j in ranked:
        for k in sorted(player):
            if k == j:
                ans.append(a[j])
            
        print(j)
        print(a[j])






    return ans

print(climbingLeaderboard())