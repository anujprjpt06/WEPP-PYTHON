#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
    #Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
    #Output:
    #UpperCase : 5
    #LowerCase : 18
    #NumberCase : 5
    #SpecialCase : 11


string = input("Enter the your own string : ")

upper_case = lower_case =  number = spl_char = 0

for i in range(len(string)):
    if string[i] >= 'A' and string[i] <= 'Z':
        upper_case += 1
    elif string[i] >= 'a' and string[i] <= 'z':
        lower_case += 1
    elif string[i] >= '0' and string[i] <= '9':
        number += 1
    else:
        spl_char += 1

print("UpperCase : ",upper_case)
print("LowerCase : ",lower_case)
print("NumberCase : ",number)
print("SpecialCase : ",spl_char)
