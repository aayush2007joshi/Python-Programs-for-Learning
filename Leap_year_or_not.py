year = int(input("Enter any year in YYYY: "))
if ((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)):
    print(year, "is Leap Year")
else:
    print(year, "is not a Leap Year")
