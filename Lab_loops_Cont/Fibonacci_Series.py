# 4. Python program to get the Fibonacci series between 0 to 50.

# The Fibonacci series is the sequence where each number is the sum of the previous two numbers of the sequence.
# The first two numbers of the Fibonacci series are 0 and 1 and are used to generate the Fibonacci series.


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

