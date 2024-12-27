# Create an application for online food ordering

# Function to handle Starter Menu
def Starter():
    # For storing the price of the selected items in Starter
    total = 0
    # Iterating over the Starter function until the 'Back to Main Menu' option is selected..
    while True:
        print("\nStarter Menu:")
        print("1: Spring Rolls -- 250 Rs.")
        print("2: Soup -- 200 Rs.")
        print("3: Garlic Bread -- 210 Rs.")
        print("4: Salad -- 150 Rs.")
        print("5: Back to Main Menu")

        # taking user input for starter menu
        userStarter = input("Select your starter from the Starter menu (1-5): ")
        if userStarter == '1':
            print("You selected Spring Rolls. Price: 250 Rs.")
            total += 250
        elif userStarter == '2':
            print("You selected Soup. Price: 200 Rs.")
            total += 200
        elif userStarter == '3':
            print("You selected Garlic Bread. Price: 210 Rs.")
            total += 210
        elif userStarter == '4':
            print("You selected Salad. Price: 150 Rs.")
            total += 150
        elif userStarter == '5':
            return total
        else:
            print("Invalid selection. Please try again.")

# Function to handle Main Course Menu
def mainCourse():
    # For storing the price of each item selected in Main Course
    total = 0
    while True:
        print("\nMain Course Menu:")
        print("1: Butter Chicken -- 200 Rs.")
        print("2: Paneer Tikka Masala -- 210 Rs.")
        print("3: Veg Biryani -- 220 Rs.")
        print("4: Chicken Biryani -- 230 Rs.")
        print("5: Back to Main Menu")

        userMainCourse = input("Select your main course from the Main course menu (1-5): ")
        if userMainCourse == '1':
            print("You selected Butter Chicken. Price: 200 Rs.")
            total += 200
        elif userMainCourse == '2':
            print("You selected Paneer Tikka Masala. Price: 210 Rs.")
            total += 210
        elif userMainCourse == '3':
            print("You selected Veg Biryani. Price: 220 Rs.")
            total += 220
        elif userMainCourse == '4':
            print("You selected Chicken Biryani. Price: 230 Rs.")
            total += 230
        elif userMainCourse == '5':
            return total
        else:
            print("Invalid selection. Please try again.")

# Function to handle Desert Menu
def Deserts():
    # For storing the price of each item selected in Desert menu
    total = 0
    while True:
        print("\nDesert Menu:")
        print("1: Ice Cream -- 100 Rs.")
        print("2: Brownie -- 150 Rs.")
        print("3: Gulab Jamun -- 120 Rs.")
        print("4: Cheesecake -- 180 Rs.")
        print("5: Back to Main Menu")

        userDesert = input("Select your desert from the menu (1-5): ")
        if userDesert == '1':
            print("You selected Ice Cream. Price: 100 Rs.")
            total += 100
        elif userDesert == '2':
            print("You selected Brownie. Price: 150 Rs.")
            total += 150
        elif userDesert == '3':
            print("You selected Gulab Jamun. Price: 120 Rs.")
            total += 120
        elif userDesert == '4':
            print("You selected Cheesecake. Price: 180 Rs.")
            total += 180
        elif userDesert == '5':
            return total
        else:
            print("Invalid selection. Please try again.")

# Function to handle Drinks Menu
def Drinks():
    # For storing the price of each item selected in Drinks menu
    total = 0
    while True:
        print("\nDrinks Menu:")
        print("1: Coffee -- 50 Rs.")
        print("2: Tea -- 30 Rs.")
        print("3: Juice -- 80 Rs.")
        print("4: Soda -- 60 Rs.")
        print("5: Back to Main Menu")

        userDrink = input("Select your drink from the menu (1-5): ")
        if userDrink == '1':
            print("You selected Coffee. Price: 50 Rs.")
            total += 50
        elif userDrink == '2':
            print("You selected Tea. Price: 30 Rs.")
            total += 30
        elif userDrink == '3':
            print("You selected Juice. Price: 80 Rs.")
            total += 80
        elif userDrink == '4':
            print("You selected Soda. Price: 60 Rs.")
            total += 60
        elif userDrink == '5':
            return total
        else:
            print("Invalid selection. Please try again.")

# Main Function to manage the application
def main():
    # Initialize the total bill amount
    total_bill = 0
    print("Welcome to My Hotel \n")

    # Iterating over the main menu until the user chooses to Bill
    while True:
        print("\nMenu Categories:")
        print("1: Starter")
        print("2: Main Course")
        print("3: Deserts")
        print("4: Drinks")
        print("5: Bill")

        choice = input("Select your option (1-5): ")

        if choice == '1':   # Naviagte to Starter Menu
            total_bill += Starter()
        elif choice == '2': # Navigate to Main Course menu
            total_bill += mainCourse()
        elif choice == '3':  # Navigate to Desert menu
            total_bill += Deserts()
        elif choice == '4': # navigate to Drinks menu
            total_bill += Drinks()
        elif choice == '5': # Display the total bill and exit
            print("Your total bill is: ", total_bill, "Rs.")
            print("Thank you for visiting My Hotel. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the application
if __name__ == '__main__':
    main()
