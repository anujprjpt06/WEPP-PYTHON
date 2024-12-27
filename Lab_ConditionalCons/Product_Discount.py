''' 4. A toy vendor supplies three types of toys: Battery Based Toys, Key-based
       Toys, and Electrical Charging Based Toys. The vendor gives a discount of
       10% on orders for battery-based toys if the order is for more than Rs. 1000.
       On orders of more than Rs. 100 for key-based toys, a discount of 5% is
       given, and a discount of 10% is given on orders for electrical charging based
       toys of value more than Rs. 500. Assume that the numeric codes 1,2 and 3
       are used for battery based toys, key-based toys, and electrical charging based
       toys respectively. Write a program that reads the product code and the order
       amount and prints out the net amount that the customer is required to pay
       after the discount.
'''

# Taking input from the user
product_code = int(input("Enter the product code (1 for Battery based Toys, 2 for Key-based Toys, 3 for Electrical based Toys) : "))
order_amount = float(input("Enter the order amount : "))

# Initializing discount
discount = 0

# applying discount based on product code and order amount

if product_code == 1 and order_amount > 1000:  # Battery based toys
    discount = 0.10 * order_amount             #  10% discount  
elif product_code == 2 and order_amount > 100: # Key based toys
    discount = 0.05 * order_amount             #  5% discount
elif product_code == 3 and order_amount > 500: # Electrical Charging based toy
    discount = 0.10 * order_amount             #  10% discount


# Calculating net amount

net_amount = order_amount - discount

print(f"The net amount to be paid after discount is : {net_amount:.2f}")
