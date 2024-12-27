# 1. Write a Python program to sum all the items in a list.

def sum_of_list(numbers):
    return sum(numbers)

input_number = input("Enter numbers separated by spaces : ")

numbers = list(map(int, input_number.split()))
total = sum_of_list(numbers)
print("Sum Of the List : ", total)


