#4. Write a Python Count vowels in a string
    #input= “Welcome to Python Assig


string = input("Enter a string : ")

vowels = 'aeiou'

ip_string = string.casefold()

count = {}.fromkeys(vowels, 0)

for char in ip_string:
    if char in count:
        count[char] += 1

print(count)
