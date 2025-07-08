import math


def getTotalX():
    a = [2, 6]
    b = [24, 36]

    def check_a(num, a):
        for i in a:
            if num % i != 0:
                return False
        return True
    
    def check_b(num, b):
        for i in b:
            if i % num != 0:
                return False
        return True

    count = 0
    for i in range(1, max(b) + 1):
        if check_a(i, a) and check_b(i, b):
            count += 1
        
    return count

print(getTotalX())