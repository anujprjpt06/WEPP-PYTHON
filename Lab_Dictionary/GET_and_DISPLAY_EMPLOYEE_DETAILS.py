##3.Write a Python program to get the key, value and item in a dictionary.
##  Accept the input as a employee details. name,no, ID, dep , des,DOJ, DOB, salary


def get_employee_details():
    # Create an empty dictionary to store employee details
    employee_details = {}
    
    # Accept employee details from the user
    employee_details['name'] = input("Enter employee name: ")
    employee_details['no'] = input("Enter employee number: ")
    employee_details['ID'] = input("Enter employee ID: ")
    employee_details['dep'] = input("Enter employee department: ")
    employee_details['des'] = input("Enter employee designation: ")
    employee_details['DOJ'] = input("Enter employee date of joining (DOJ): ")
    employee_details['DOB'] = input("Enter employee date of birth (DOB): ")
    employee_details['salary'] = input("Enter employee salary: ")
    
    return employee_details

def display_employee_details(employee_details):
    # Print the key, value, and item for each entry in the dictionary
    for key, value in employee_details.items():
        print(f"\nKey: {key}, Value: {value}, Item: ({key}, {value})")

# Example usage
employee_details = get_employee_details()
display_employee_details(employee_details)
