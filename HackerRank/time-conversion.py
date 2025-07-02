def timeCon():
    # s = '12:01:00PM' #12:01:00
    s = '12:01:00PM' #00:01:00

    if s[-2:] == 'AM' and s[:2] == '12':
        return "00" + s[2:-2]
    
    elif s[-2:] == 'AM':
        return s[:-2]

    elif s[-2:] == 'PM' and s[:2] == '12':
        return s[:-2]

    else:
         return str(int(s[:2]) + 12) + s[2:-2]

print(timeCon())