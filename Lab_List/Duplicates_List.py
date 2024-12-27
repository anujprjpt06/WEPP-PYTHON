# 3. Write a Python program to find duplicate values from a list and display those.

NumList = []

Number = int(input("Please enter the Total Number of List Elements : "))
for i in range(1, Number + 1):
    value = int(input("Please enter the value of %d Element : " %i))
    NumList.append(value)


NumList.sort()
print(NumList)

dupItems = []
uniqItems = {}

for x in NumList:
    if x not in uniqItems:
        uniqItems[x] = 1
    else:
        if uniqItems[x] == 1:
            dupItems.append(x)
        uniqItems[x] += 1

print("Duplicate Elements : ",dupItems)
