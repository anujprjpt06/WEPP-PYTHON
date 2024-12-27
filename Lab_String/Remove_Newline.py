# 2. Write a Python program to remove a newline in Python.
#    String = "\nBest \nDeeptech \nPython \nTraining\n"

def remove_newline(string):
    return string.replace('\n','')

input_string = input("Enter a string : ")

print(remove_newline(input_string))

