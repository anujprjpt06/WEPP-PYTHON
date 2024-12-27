# 3. Python program to check if a given number is an Armstrong number.

# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits.
# For example, the number 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153
# Armstrong number is also known as the narcissistic number, plusperfect digital invariant (PPDI), or plus perfect number.


Check_Armstrong_Number = int(input("Enter a number : "))
num = Check_Armstrong_Number
digit , armstrong_sum = 0, 0

length = len(str(num))

for i in range(length):
    digit = num % 10
    num = num // 10
    armstrong_sum += pow(digit, length)

if armstrong_sum == Check_Armstrong_Number:
    print("It is an Armstrong Number : ",Check_Armstrong_Number)
else:
    print("Not an Armstrong Number : ",Check_Armstrong_Number)
    
