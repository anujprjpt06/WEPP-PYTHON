# 4. Write a Python program to count and display the vowels of a given text.
# String=”Welcome to python Training”

def Check_vowels(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)

string = input("Enter a string : ")
vowels = "AaEeIiOoUu"
Check_vowels(string, vowels)
