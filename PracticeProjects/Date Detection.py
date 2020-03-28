import re

date = "30/04/2100"
error = "Not a compatible date :("
success = "Compatible!"
shortMonths = [4, 6, 9, 11]
regex = re.compile(r'''([0-2][1-9]|[1-3][0]|31)  # day
                /  # divider
                ([0][1-9]|[1][0-2])  # month
                /  # divider
                [12]\d{3}''', re.VERBOSE)  # year
if regex.match(date):
    dateArray = date.split("/")
    for x in range(2):
        try:
            if int(dateArray[x]) > 9:
                pass
        except TypeError:
            dateArray[x] = dateArray[x][1]
    date, month, year = dateArray
    date, month, year = int(date), int(month), int(year)
    # eliminates all dates that are too high except the non leap year Feb 29th
    if month in shortMonths and date > 30 or month == 2 and date > 29:
        print(error)
    elif month == 2 and date == 29:
        if year % 4 == 0 and year % 100 != 0:  # check if leap day
            print("happy leap day")
            print(success)
        elif year % 400 == 0:
            print(success)
        else:
            print(error)
    else:
        print(success)
else:
    print(error)

