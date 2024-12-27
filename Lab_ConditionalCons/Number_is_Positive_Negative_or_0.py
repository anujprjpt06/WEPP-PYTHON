# 3. Python Program to Check if a Number is Positive, Negative or 0

# Taking number as input from the user
number = int(input("Enter the year : "))

# Finding positive number 
if number > 0:
    print(f"{number} is a Positive number")
elif number < 0:
    print(f"{number} is a Negative number")
else:
    print("The number is zero")
