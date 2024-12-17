##-------- Q2 ----------
##----*
##---**
##--***
##-****
##*****

def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(' ' * (rows - i), end='')
        # Print asterisks
        print('*' * i)

# Take input from the user
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)
