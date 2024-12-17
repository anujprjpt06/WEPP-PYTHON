##--------- Q3 -----------
##1
##10
##101
##1010
##10101

def print_binary_triangle(rows):
    for i in range(1, rows + 1):
        pattern = ''
        for j in range(1, i + 1):
            pattern += str(j % 2)
        print(pattern)

# Take input from the user
rows = int(input("Enter the number of rows: "))

# Print the pattern
print_binary_triangle(rows)

