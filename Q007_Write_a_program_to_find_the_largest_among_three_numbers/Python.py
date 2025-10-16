# Q007 Write a program to find the largest among three numbers

number1 = int(input("Enter first Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

if ( number1 > number2 and number2 > number3):
    print(f'{number1} is Greater than among {number1 , number2 , number3}')

elif(number2 > number1 and number1 > number3):
    print(f'{number2} is Greater than among {number1 , number2 , number3}')
else:
    print(f'{number3} is Greater than among {number1 , number2 , number3}')