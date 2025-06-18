print("Leap Year Check")
year_x = int(input("Enter a year: "))

if ((year_x % 4 == 0 and year_x % 100 != 0))\
    or (year_x % 400 == 0):
    print(year_x, "is a leap year.")

else:
    print(year_x, "is not a leap year.")

print("Thanks!")