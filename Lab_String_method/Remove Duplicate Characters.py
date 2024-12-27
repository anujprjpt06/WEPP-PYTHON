#2. Write a Python program to remove duplicate characters of a given string.
    #Input = “String and String Function”
    #Output: String and Function

string = input("Enter a string : ")
p = ""

for char in string:
    if char not in p:
        p = p+char

print(p)

