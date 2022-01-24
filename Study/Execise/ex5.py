
print("Count days in month")
month = int(input("Enter month: "))
if (month == 1 and month == 3 and month == 5 and month == 7 and 
    month == 8 and month == 10  and month == 12):
    print(f"{month} has 31 days")
elif (month == 4 and month == 6  and month == 9 and month == 11):
    print(f"{month} has 30 days")
else:
    year = int(input("Enter year: "))
    if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
        print("Month has 29 days")
    else:
        print("Month has 28 days")
    