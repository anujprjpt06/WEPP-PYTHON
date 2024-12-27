# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

# Take 5 numbers as input from the user
numbers = []
for i in range(5):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Display the numbers
print("Numbers:", numbers)

# Find and display the maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)

print("Maximum Value:", max_value)
print("Minimum Value:", min_value)


    
