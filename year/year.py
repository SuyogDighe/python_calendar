import calendar as cal

def years():
    year=int(input("Enter the year: "))
    print(f"\nEntire Calendar for year {year}:")
    print(cal.calendar(year))