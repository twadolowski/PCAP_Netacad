def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True


def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    else:
        return 30


def day_of_year(year, month, day):
    days = 0
    for i in range(1, month):
        days += days_in_month(year, i)
    return days + day


print(day_of_year(2001, 12, 31))


# Test
def test_day_of_year():
    assert day_of_year(2000, 1, 1) == 1
    assert day_of_year(2000, 1, 31) == 31
    assert day_of_year(2000, 2, 1) == 32
    assert day_of_year(2000, 2, 29) == 60
    assert day_of_year(2000, 3, 1) == 61
    assert day_of_year(2000, 12, 31) == 366
    assert day_of_year(1900, 1, 1) == 1
    assert day_of_year(1900, 12, 31) == 365
    assert day_of_year(2001, 1, 1) == 1
    assert day_of_year(2001, 12, 31) == 365
    assert day_of_year(2020, 2, 29) == 60
    assert day_of_year(2021, 2, 28) == 59
    assert day_of_year(2021, 12, 31) == 365
