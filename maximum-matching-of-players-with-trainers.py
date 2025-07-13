def matchPlayersAndTrainers():
    players = [4,7,9] 
    trainers = [8,2,5,8] #2

    ans = 0

    players.sort()
    trainers.sort()

    for i, trainer in enumerate(trainers):
        if players[ans] <= trainer:
            ans += 1
            if ans == len(players):
                return ans

    return ans

print(matchPlayersAndTrainers())