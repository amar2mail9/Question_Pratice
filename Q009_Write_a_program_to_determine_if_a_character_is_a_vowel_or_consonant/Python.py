# Write a program to determine if a character is a vowel or consonant.
char = input("Enter a Character: ").lower()

if len(char)==1 and char.isalpha():
    if char in ["a", "e", "i", "o", "u"]:
        print(f"{char} is vowel")
    else:
        print(f"{char} is constant")
else:
    print("Enter alphabet and single alphabet only")