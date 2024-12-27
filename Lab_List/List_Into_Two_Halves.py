# 4. Write a Python program to split a given list into two parts where the length of the first part of the list is given.

def split_list(input_list, first_part_length):

    first_part = input_list[:first_part_length]
    second_part = input_list[first_part_length:]
    return first_part , second_part

original_list = [1,1,2,3,4,4,5,1]

part_length = 3

first_part , second_part = split_list(original_list, part_length)

print("Original List")
print(original_list)
print("\nLength of the first part of the list : ",part_length)
print("\nSplitted the said list into two parts : ")
print((first_part, second_part))
