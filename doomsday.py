# Implemented straight from https://en.wikipedia.org/wiki/Doomsday_rule
days = 'SUNDAY MONDAY TUESDAY WEDNESDAY THURSDAY FRIDAY SATURDAY'.split()
def doomsday (year):
    # determine century anchor
    #Note, year works if >=1600
    cent_anchor = [2,0,5,3][(year // 100)%4]
    # variable names are from wiki
    a = (year % 100) // 12 # same as floor because year should be positive
    b = (year % 100) % 12
    c = b // 4
    d = a+b+c
    day_idx = (cent_anchor+d)%7
    return day_idx
    
def day_of_week(day, month, year):
    dday = doomsday(year)
    # there is no zero month, but makes indexing easier
    first_dd = [0,3,7,7,4,2,6,4,1,5,3,7,5]
    # check for leapyear
    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        first_dd[1] = 4
        first_dd[2] = 1
    # the + 7 accounts for if the day is before the first doomsday
    return ((day - first_dd[month]+7) + dday)%7

if __name__=='__main__':
    for i in range(1702, 1707):
        print(doomsday(i))
    print(doomsday(1946))
    print(days[day_of_week(12,4,1861)])
    print(days[day_of_week(18,9,1985)])