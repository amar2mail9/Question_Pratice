#Q006 Write a program to check if a number is even or odd

# take number by user
number = int(input("Enter any positive Number: "))

if number > 0:
    if number % 2 == 0 :
        print(f"{number }  number is Even")
    else:
        print(f"{number}  number is odd")
else:
    print("Enter ony Positive and Natural Number")