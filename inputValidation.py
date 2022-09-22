import datetime
import doomsday

def validate(name, favday, birthday):
    valid = True
    values_invalid = []
    favday = favday.upper()
    
    day, month, year = birthday.split('/')
    if(not(name.isalpha())):
        valid = False
        values_invalid.append("name")

    if (not(favday.isalpha()) or not(favday in doomsday.days)):
        valid = False
        values_invalid.append("favorite day")

    if (not(datetime.datetime(int(year), int(month), int(day)))):
        valid = False
        values_invalid.append("birthday")
    
    result = [valid, values_invalid]
    return result
