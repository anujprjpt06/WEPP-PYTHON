# 4. Python program to find the area of a triangle whose sides are given

# Python Program to find the area of triangle

a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)


# Note - %0.2f floating-point specifies at least 0 wide and 2 numbers after the decimal.
#        If you use %0.5f, then it will give 5 numbers after the decimal.
