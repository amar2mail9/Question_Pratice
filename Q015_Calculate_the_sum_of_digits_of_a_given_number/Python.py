# Q015_Calculate_the_sum_of_digits_of_a_given_number

number = int(input("Enter a Number:"))

sum = 0;
for i in str(number):
    sum += int(i)

print(sum)