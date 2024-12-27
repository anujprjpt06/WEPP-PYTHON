# 2. Using input function take two number and then swap the number

# Taking two numbers from the user
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

print(f"Before swapping: number1 = {number1}, number2 = {number2}")

# Swapping the numbers
number1, number2 = number2, number1

print(f"After swapping: number1 = {number1}, number2 = {number2}")
