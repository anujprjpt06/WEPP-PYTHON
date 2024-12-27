# 2. Python program to check if the given string is a palindrome.

# A palindrome is a sequence of characters that reads the same backward as forward.
# This can include words, numbers, phrases, or other sequences of symbols.
# For example, the words "madam," "racecar," and the number "12321" are all palindromes.

string = input("Enter your letter : ")
string1 = string.casefold()

# this string is reverse.
reverse = reversed(string)

if list(string) == list(reverse):
    print("The letter is a palimndrome")

else:
    print("The letter is not a palindrome")

