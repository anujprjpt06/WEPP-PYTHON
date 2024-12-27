# 1. Declare a div() function with two parameters.
#    Then call the function and pass two numbers and display their division.

def div(number1,number2):
    division = number1/number2
    print(f"Division of two numbers {number1} & {number2} is {division}")

userInput1 = int(input("Enter the first number : "))
userInput2 = int(input("Enter the second number : "))

div(userInput1,userInput2)

    
