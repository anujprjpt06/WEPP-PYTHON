# 2. Write a Python program to get the largest and smallest number from a list
#    without built-in functions.


NumList = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the value of %d Element : " %i))
    NumList.append(value)


NumList.sort()
print(NumList)

print("\nThe Smallest Element in this List is : ",NumList[0])
print("The Largest Element in this List is : ",NumList[Number - 1])
