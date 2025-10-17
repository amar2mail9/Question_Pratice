# Q017_Count_the_number_of_vowels_in_a_given_string

string = input("Enter Word: ").lower()
count = 0
if type(string) == str:
    for i in string:
     if i in ["a","e","o", 'i', "u"]:
        count +=1
        print(i)
else:
   print("Number not allow")

print(f"Count {count}")