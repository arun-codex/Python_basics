# 6. Return whether a year is a leap year.
# leap year is divide by 4 and 400 but not divide by 100

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return f"{year} is leap year."
            else: 
                return f"{year} is not leap year."

        return f"{year} is leap year."
    else:
        return f"{year} is not leap year."

year = 2032

leap = leap_year(year)

print(leap)
