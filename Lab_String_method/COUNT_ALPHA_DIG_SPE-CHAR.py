#1. Write a Python program to Count all letters, digits, and special symbols from the given string
    #Input = “P@#yn26at^&i5ve”
    #Output: Chars = 8 Digits = 2 Symbol = 3


string = input("Enter your own string : ")
alphabets = digits = special = 0

for i in range(len(string)):
    if(string[i].isalpha()):
        alphabets += 1
    elif(string[i].isdigit()):
        digits += 1
    else:
        special += 1

print("\nTotal Number of Char in this String : ",alphabets)
print("Total Number of Digits in this String : ",digits)
print("Total Number of Special Characters in this String : ",special)
