# 3. Write a Python program to reverse words in a string.
#  String = “Deeptech Python Training”


def reverse_words(string):

    words = string.split()

    reversed_words = words[::-1] # Reverse the list of words

    reversed_string = ' '.join(reversed_words)

    return reversed_string

input_string = input("Enter a string : ")
print("Reversed Words : ", reverse_words(input_string))
