# 5. Python program to check the validity of password input by users.

# The re module in Python provides support for working with regular expressions, which are sequences of characters that define search patterns.
# Regular expressions are powerful tools for matching, searching, and manipulating text based on specific patterns.


import re

def check_password_validity(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Password must contain at least one special character."
    
    return "Password is valid."

# Take input from the user
password = input("Enter your password: ")

# Check the validity of the password
result = check_password_validity(password)
print(result)
