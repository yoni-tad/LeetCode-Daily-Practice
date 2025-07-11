def dayOfProgrammer():
    year = 1800
    isLeap = False

    def checkLeap(year, calendar):
        if calendar == 'Julian':
            if year % 4 == 0:
                return True
            else:
                return False
        else:
            if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
                return True
            else: 
                return False

    if year <= 1917:
        isLeap = checkLeap(year, 'Julian')
    elif year == 1918:
         return '26.09.' + str(year)
    else:
        isLeap = checkLeap(year, 'Gregorian')


    if isLeap:
        return '12.09.' + str(year)
    else:
        return '13.09.' + str(year)

print(dayOfProgrammer())