# Q012_Print_all_even_numbers_between_1_and_50

starting_Number = int(input("Enter Starting Number: "))
ending_Number = int(input("Enter Ending Number: "))

if starting_Number > ending_Number :
    print ("Starting number should be less than or equal to ending number.")
else:

    for i in range(starting_Number, ending_Number+1):
        if i % 2 == 0:
            print(f"Even Number : {i}")
        
    