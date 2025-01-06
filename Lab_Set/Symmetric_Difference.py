#  2. Write a Python program to Return a set of elements present in Set A or B, but not both.

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

# Get the elements that are in set1 or set2 but not in both (symmetric difference)
result = set1.symmetric_difference(set2)

print("Output:", result)


##The symmetric_difference() method is used to find the elements that are present in either set1 or set2, but not in both.
##This returns a set with unique elements from both sets.
