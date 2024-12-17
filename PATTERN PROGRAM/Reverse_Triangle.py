##---------- Q1 ---------------
##*******
##******
##*****
##****
##***
##**
##*

def print_pattern(rows):
    for i in range(rows, 0 , -1):
        print('*' * i)

rows = int(input("Enter the number of rows : "))
print_pattern(rows)
