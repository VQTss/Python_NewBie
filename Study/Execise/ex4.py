print("Enter year and check that year. Is it leap year")
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0):
    print("This year is leap year")
else:
    print("This year is not leap year")