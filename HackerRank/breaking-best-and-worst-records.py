def breakingRecords():
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]  


    best = scores[0]
    worst = scores[0]
    best_count = 0
    worst_count = 0
    for i in scores:
        if i > best:
            best_count += 1
            best = i
        
        if i < worst:
            worst_count += 1
            worst = i
            
    return [best_count, worst_count]

print(breakingRecords())