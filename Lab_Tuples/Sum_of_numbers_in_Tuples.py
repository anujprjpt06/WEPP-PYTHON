# 3. Write a Python program to calculate the sum of the numbers in a given tuple.

tuples_list = [(1,2),(3,4),(5,6)]

# Using the sum() method and list comprehension

# Calculate the sum of all numbers in the tuple
total_sum = sum(sum(t) for t in tuples_list)

print("Sum of values in the tuples : ",total_sum)

### Second Method
### We can done also using the nestes loops .
##total_sum = 0
##
##for subtuple in tuples_list:
##    for item in subtuple:
##        total_sum += item
##
##        
##print("Sum of values in the tuples : ",total_sum)

        
