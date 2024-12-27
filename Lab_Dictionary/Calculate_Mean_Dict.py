##1. Write a Python program and calculate the mean of the below dictionary.
##   Accept student name as key and in value accept marks


def calculate_mean(marks_dict):
    total_marks = sum(marks_dict.values())

    num_students = len(marks_dict)

    mean_marks = total_marks / num_students

    return mean_marks

marks_dict = {}
num_students = int(input("Enter the number of students : "))

for _ in range(num_students):
    name = input("Enter Student name : ")
    marks = float(input("Enter marks : "))
    marks_dict[name] = marks


mean_marks = calculate_mean(marks_dict)
print("Mean of the marks : ", mean_marks)
    
