import datetime
import doomsday

def validate(name, favday, birthday):
    valid = True
    values_invalid = []
    favday = favday.upper()
    
    day, month, year = birthday.split('/')
    if(not(name.isalpha())):
        valid = False
        values_invalid.append("INVALID NAME")

    if (not(favday.isalpha())):
        valid = False
        values_invalid.append("INVALID FAVORITE DAY") 
    elif (not(favday in doomsday.days)):
        valid = False
        values_invalid.append("INVALID FAVORITE DAY") 

    validDate = True #change the date validation for months
    if (not(datetime.datetime(int(year), int(month), int(day)))):
        valid = False
        values_invalid.append("INVALID DATE")
    try:
        day, month, year = birthday.split('/')
        datetime.datetime(int(year), int(month), int(day)) #checking if the date is valid using the datetime module
    except ValueError:
        values_invalid.append("INVALID DATE")

    result = [valid, values_invalid]
    return result

def datefound(birthday):
    day, month, year = birthday.split('/')
    datefound = doomsday.doomsday(int(year))
    return datefound
