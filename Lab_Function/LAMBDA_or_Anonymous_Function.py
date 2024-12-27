# 5. Write a lambda function that takes one argument and returns 'Positive' if the number is greater than 0, 'Negative' if it's less than 0, and 'Zero' if it's 0.
#    Test it with different numbers.

# Define the lambda function
check_number = lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Zero')

number = float(input("Enter a number: "))

result = check_number(number)

print("The number is:", result)


    
