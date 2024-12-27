# 1. Python program to check leap year

# User to enter a year
year = int(input("Enter the year : "))

# Checking if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# A year is a leap year if:
# It is divisible by 4 and not divisible by 100, or
# It is divisible by 400.
