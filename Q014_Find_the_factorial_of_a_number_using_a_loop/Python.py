# Q014_Find_the_factorial_of_a_number_using_a_loop

number = int(input("Enter number: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
    exit()

if number >= 1000:
    print("Enter only a three-digit number or less.")
    exit()

if number == 0 or number == 1:
    print("Factorial is 1")
    exit()

fact = 1
for i in range(1, number + 1):
    fact *= i

print(f"Factorial of {number} is {fact}")
