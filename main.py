import calendar as cal
from month import month
from year import year

num=input("Year for y or month for m: ")
if(num=="y"):
    year.years()
elif(num=="m"):
    month.months()
# else:
#     exit()