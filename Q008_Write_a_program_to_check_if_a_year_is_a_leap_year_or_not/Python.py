# Q008 Write a program to check if a year is a leap year or not

year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")
