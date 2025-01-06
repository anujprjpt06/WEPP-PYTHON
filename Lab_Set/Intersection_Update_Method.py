# 4. Write a Python program to Remove items from set1 that are not common to both set1 and set2.

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

# Keep only the common elements in set1
set1.intersection_update(set2)

print(set1)


##The intersection_update() method modifies set1 to keep only the elements that are present in both set1 and set2.
