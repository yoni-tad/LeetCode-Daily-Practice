def gradingStudents():
    n = 4
    grades = [73, 67, 38, 33]

    ans = []
    for i in grades:
        if (i + 3) < 40:
            ans.append(i)
        else:
            found = False
            for j in range(1, 3):
                if (i + j) % 5 == 0:
                    ans.append(i + j)
                    found = True
           
            if not found:
                ans.append(i) 
    return ans

print(gradingStudents())