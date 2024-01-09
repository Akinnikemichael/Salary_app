from class_employee import employee
import datetime
import calendar

name = input("what is the your name? ")
department = input("what is your department? ")
level = input("what level are you on XYZ and co salary scale? ")
bank_name = input("what is the name of your bank? ")
account_number = input("what is your account number? ")
time = input("is today the last day of the month? ")




x = datetime.datetime.now()
a = calendar.monthrange(x.year, x.month)[1]


print(a)




Employee1 = employee("Tobi", "product", "one", "Zenith", "123456789", True)
Employee2 = employee("Michael", "product", "two", "FCMB", "987456321", True)
Employee3 = employee("Segun", "product", "three", "First bank", "652398741", True)

if x != a:
        #and y != a and is_today_last_day_of_the_month == False):
    print("Not pay day, you will be paid on the last day of the month")
elif level == "one":
    print("you have just been paid N50,000")
elif level == "two":
    print("you have just been paid N100,000")
elif level == "three":
    print("you have just been paid N150,000")







