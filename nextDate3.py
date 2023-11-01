def check(day, month):
    return (month in [4, 6, 9, 11]) and (day == 31)

def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

day, month, year, tomm_day, tomm_month, tomm_year = 0, 0, 0, 0, 0, 0

while True:
    day, month, year = map(int, input("Enter today's date in the form of dd mm yyyy: ").split())
    tomm_month, tomm_year = month, year

    if day < 1 or day > 31 or (month not in range(1, 13)) or check(day, month) or (year <= 1812 or year > 2015):
        print("Invalid date input")
    else:
        break

day += 1

if day > 30 or (month == 2 and (isleap(year) and day > 29 or not isleap(year) and day > 28)):
    day, tomm_month = 1, month + 1

if month == 12 and day == 1:
    tomm_month, tomm_year = 1, year + 1

print(f"Next day is: {day} {tomm_month} {tomm_year}")


# Longer Version

def check(day, month):
    return (month in [4, 6, 9, 11]) and (day == 31)

def isleap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

day, month, year, tomm_day, tomm_month, tomm_year = 0, 0, 0, 0, 0, 0
flag = 'y'

while flag == 'y':
    flag = 'y'
    day, month, year = map(int, input("Enter today's date in the form of dd mm yyyy: ").split())
    tomm_month, tomm_year = month, year

    if day < 1 or day > 31:
        print("Value of day not in the range 1...31")
        flag = 'n'

    if month < 1 or month > 12:
        print("Value of month not in the range 1...12")
        flag = 'n'
    elif check(day, month):
        print("Value of day not in the range day <= 30")
        flag = 'n'

    if year <= 1812 or year > 2015:
        print("Value of year not in the range 1812...2015")
        flag = 'n'

    if month == 2:
        if isleap(year) and day > 29:
            print("Invalid date input for a leap year")
            flag = 'n'
        elif not isleap(year) and day > 28:
            print("Invalid date input for a non-leap year")
            flag = 'n'

months_with_31_days = {1, 3, 5, 7, 8, 10}
months_with_30_days = {4, 6, 9, 11}

if month in months_with_31_days:
    tomm_day = day + 1 if day < 31 else 1
    if day >= 31:
        tomm_month = month + 1

elif month in months_with_30_days:
    tomm_day = day + 1 if day < 30 else 1
    if day >= 30:
        tomm_month = month + 1

elif month == 12:
    tomm_day = day + 1 if day < 31 else 1
    if day >= 31:
        tomm_month = 1
        if year == 2015:
            print("The next day is out of the boundary value of the year")
            tomm_year = year + 1
        else:
            tomm_year = year + 1

elif month == 2:
    if day < 28:
        tomm_day = day + 1
    elif isleap(year) and day == 28:
        tomm_day = day + 1
    else:
        tomm_day = 1
        tomm_month = 3

print(f"Next day is: {tomm_day} {tomm_month} {tomm_year}")

