#2. Declare a square() function with one parameter.
#   Then call the function and pass one number and display the square of that number .

def square(number1):
    square = number1 ** 2  # or number1 * number1
    print(f"Square of number {number1} is {square}")

userInput1 = int(input("Enter the number that you want to square : "))

square(userInput1)
    
