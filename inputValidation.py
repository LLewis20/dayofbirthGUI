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

    try:
        day, month, year = birthday.split('/')
        datetime.datetime(int(year), int(month), int(day)) #checking if the date is valid using the datetime module
    except ValueError:
        date = input("PLEASE ENTER A VALID DATE!!\nPlease enter your birthday(dd/mm/yyyy):")
        valid = False

    result = [valid, values_invalid]
    return result

def datefound(birthday):
    day, month, year = birthday.split('/')
    datefound = doomsday.days[doomsday.day_of_week(int(day),int(month),int(year))]
    return datefound
