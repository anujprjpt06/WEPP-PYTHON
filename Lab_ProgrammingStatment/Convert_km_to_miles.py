# 3. Write a Program to Convert Kilometers to Miles

# Taking input from the user
kilometers = float(input("Enter the distance in kilometers: "))

# Conversion factor
conversion_factor = 0.621371

# Converting kilometers to miles
miles = kilometers * conversion_factor

# Displaying the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
