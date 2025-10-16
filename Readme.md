<ol>

<h3><li>**Write a Python program to take two numbers as input and print their sum.**</li></h3>

```python
num1 = int(input("Enter First Number: "))
num2  = int((input("Enter Second Number: ")))

sum = num1 + num2

print(f'Sum of {num1} and {num2} : {sum}')

```

<h3><li>**Write a program to swap two numbers without using a third variable.**</li></h3>

```python
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter first Number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2


print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
```

<h3><li>**Write a program to find the area of a circle from the given radius.**</li></h3>

```python
PI  = 3.14

radius  = int(input('Enter Radius of Circle :'))

area = PI * radius ** 2

print(f"Area of circle {radius} radius is :", area)
```

<h3><li>**Write a program to convert temperature from Celsius to Fahrenheit **</li></h3>

```python
cel = float(input("Enter celsius :"))
far = (cel * 1.8) +32

print("Fahrenheit: ", far)
```

<h3><li>**Write a Python program to check if a number is positive, negative, or zero.**</li></h3>

```python
num = int(input("Enter any Number: "))

if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print("Enter value are Zero")

```

<h3><li>**Write a Python program to check if a number is even or odd.**</li></h3>

```python
number = int(input("Enter any positive Number: "))

if number > 0:
    if number % 2 == 0 :
        print(f"{number }  number is Even")
    else:
        print(f"{number}  number is odd")
else:
    print("Enter only Positive and Natural Number")
```

<h3><li>**Write a Python program to find the largest of three numbers.**</li></h3>

```python
number1 = int(input("Enter first Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))

if ( number1 > number2 and number2 > number3):
    print(f'{number1} is Greater than among {number1 , number2 , number3}')

elif(number2 > number1 and number1 > number3):
    print(f'{number2} is Greater than among {number1 , number2 , number3}')
else:
    print(f'{number3} is Greater than among {number1 , number2 , number3}')
```

<h3><li>**Write a program to check if a year is a leap year or not**</li></h3>

```python


year = int(input("Enter Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is Not a Leap Year")

```

<h3><li>Write a program to determine if a character is a vowel or consonant.</li></h3>

```python
char = input("Enter a Character: ").lower()

if len(char)==1 and char.isalpha():
    if char in ["a", "e", "i", "o", "u"]:
        print(f"{char} is vowel")
    else:
        print(f"{char} is constant")
else:
    print("Enter alphabet and single alphabet only")
```

<li><h3>Write a program to calculate a student's grade based on percentage marks.
</h3></li>

```python
# Write a program to calculate a student's grade based on percentage marks.

# user marks enter
hindiMarks = int(input("Enter Hindi Total Marks: "))
hindiObtained = int(input("Enter Hindi Obtained Marks: "))

englishMarks = int(input("Enter English Total Marks: "))
englishObtained = int(input("Enter English Obtained Marks: "))

mathMarks = int(input("Enter Math Total Marks: "))
mathObtained = int(input("Enter Math Obtained Marks: "))

scienceMarks = int(input("Enter Science Total Marks: "))
scienceObtained = int(input("Enter Science Obtained Marks: "))

socialScienceMarks = int(input("Enter Social Science Total Marks: "))
socialScienceObtained = int(input("Enter Social Science Obtained Marks: "))

passingPercentage = int(input("Enter Passing Percentage: "))

totalMarks = hindiMarks + englishMarks + mathMarks + scienceMarks + socialScienceMarks
obtainedMarks = hindiObtained + englishObtained + mathObtained + scienceObtained + socialScienceObtained

percentageGain = round((obtainedMarks / totalMarks) * 100, 2)

grade = "None"
status = "None"

if (
    (hindiObtained / hindiMarks * 100) >= passingPercentage and
    (englishObtained / englishMarks * 100) >= passingPercentage and
    (mathObtained / mathMarks * 100) >= passingPercentage and
    (scienceObtained / scienceMarks * 100) >= passingPercentage and
    (socialScienceObtained / socialScienceMarks * 100) >= passingPercentage
):

    if percentageGain >= 90:
        grade = "A+"
    elif percentageGain >= 80:
        grade = "A"
    elif percentageGain >= 70:
        grade = "B+"
    elif percentageGain >= 60:
        grade = "B"
    elif percentageGain >= 50:
        grade = "C+"
    elif percentageGain >= 40:
        grade = "C"
    else:
        grade = "D"

    status = "Pass"
else:
    status = "Fail"

print("\nSubject Name\tTotal Marks\tObtained Marks")
print(f"Hindi\t\t{hindiMarks}\t\t{hindiObtained}")
print(f"English\t\t{englishMarks}\t\t{englishObtained}")
print(f"Maths\t\t{mathMarks}\t\t{mathObtained}")
print(f"Science\t\t{scienceMarks}\t\t{scienceObtained}")
print(f"Social Science\t{socialScienceMarks}\t\t{socialScienceObtained}")
print('------------------------------------------')
print(f'Total Marks : {totalMarks}')
print(f'Obtained Marks : {obtainedMarks}')
print(f'Percentage : {percentageGain}%')
print(f'Grade : {grade}')
print(f'Status : {status}')

```

</ol>
