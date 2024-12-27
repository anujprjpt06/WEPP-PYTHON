# 5. Write a Python program to traverse a given list in reverse order, and print the elements with the original index.

def reverse_element(color_list):
    print("\nTraverse the list in reverse order with original index : ")
    for i in range(len(color_list) - 1,-1,-1):
        print(f"Index {i} : {color_list[i]}")

color_list = input("Enter colors separated by spaces : ").split()

print("\nOriginal List:")
print(color_list)

reverse_element(color_list)    

