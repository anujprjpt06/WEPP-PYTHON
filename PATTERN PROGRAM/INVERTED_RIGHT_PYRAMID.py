##-------- Q5 ---------
##*********
##-*******
##--*****
##---***
##----*


# Function to print inverted full pyramid pattern
def inverted_full_pyramid(n):
    for i in range(rows, 0, -1):
        for j in range(n - i):
            print(" ", end="")
        for k in range(2*i - 1):
            print("*", end="")
        print("")

rows = int(input("Enter the number of rows : "))

inverted_full_pyramid(rows)




