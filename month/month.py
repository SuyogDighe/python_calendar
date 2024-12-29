import calendar as cal

def months():
    year= int(input("Enter the year: "))
    month=int(input("Enter the month: "))
    print(f"\nCalendar for {cal.month_name[month]} {year}:")
    print(cal.month(year,month))