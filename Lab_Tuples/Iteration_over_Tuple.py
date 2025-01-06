# 4.Write a python program and iterate the given tuples

employee1 = ("John Doe",101,"Human Resources",60000)
employee2 = ("Alice Smith",102,"Marketing",55000)
employee3 = ("Bob Johnson",103,"Engineering",75000)


# Combine all employees into a list for iteration

employees = [employee1,employee2,employee3]

print("Employee Records : \n")

# Iterate through each employee tuple
for employee in employees:
    name, emp_id, department, salary = employee
    print("Name : ",name)
    print("Employee ID : ",emp_id)
    print("Department : ",department)
    print("Salary : $",salary,"\n")
    
