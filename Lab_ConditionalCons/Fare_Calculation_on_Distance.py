''' 5. A transport company charges the fare according to following table:
    Distance
    1-50
    51-100
    Charges
    8 Rs./Km
    10 Rs./Km
    > 100
    12 Rs/Km
'''

# Taking input from the user
distance = float(input("Enter the distance traveled (in km): "))

# Calculate the fare based on the distance

if distance <= 50:
    fare = distance * 8  # Rs. 8 per km
elif (distance >= 51) and (distance <= 100):
    fare = distance * 10 # Rs. 10 per km
else:  # distance > 100
    fare = distance * 12 # rs. 12 per km

print(f"The total fare is : Rs. {fare:.2f}")
