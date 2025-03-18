# 1
def season(month):
    if month in [12, 1, 2]:
        return "Kysh"
    elif month in [3, 4, 5]:
        return "Jaz"
    elif month in [6, 7, 8]:
        return "Jay"
    elif month in [9, 10, 11]:
        return "Kuz"
    else:
        return "Belgisiz ay"

print(season(3))
print(season(7))
print(season(12))
print(season(14))


# 2

def date(day, month, year):
    days_in_month = {1: 31, 2: 28, 3:31, 4:30, 5:31, 6:30,
                     7:31, 8:31, 9:30, 10:31, 11:30, 12:31 }
    if month < 1 or month > 12:
        return False

    if month == 2:
        if year % 4 == 0:
            days_in_month[2] = 29


    if day < 1 or day > days_in_month[month]:
        return False

    return True

print(date(29, 2, 2020))
print(date(30, 2, 2021))
print(date(31, 4, 2023))
print(date(15, 8, 2023))