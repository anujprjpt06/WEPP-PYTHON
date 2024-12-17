##-------- Q4 -------
##____1
##___01
##__101
##_0101
##10101

def print_pattern(rows):
    for i in range(1, rows + 1):
        # Print leading spaces
        print(' ' * (rows - i), end='')
        # Print alternating 1s and 0s
        for j in range(1, i + 1):
            print(j % 2, end='')
        print()

# Take input from the user
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_pattern(rows)


