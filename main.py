import doomsday
import inputValidation as iv

username = input("Please enter your first name: ")
birthday = input("Please enter your birthday(dd/mm/yyyy): ")
favday = input("Please enter your favorite day: ")

day, month, year = birthday.split('/')
datefound = doomsday.days[doomsday.day_of_week(int(day),int(month),int(year))]
print("\n-------------------USER'S BIRTHDAY----------------------------")
print(doomsday.zellersAlgorithm(int(day),int(month),int(year)))
if(datefound == favday):
    print("\n"+username, "you were born on a",(datefound.lower()).title(),"\nCongrats you were born on your favorite day \N{thumbs up sign}!!!!")
else:
    print("\n"+username, "you were born on",(datefound.lower()).title(),"\nUnfortunately you were not born on your favorite day")


print("\n--------------------FICTIONAL USER'S BIRTHDAY---------------------------")
print(doomsday.days[doomsday.day_of_week(12,4,1861)])
print(doomsday.days[doomsday.day_of_week(18,9,1985)])