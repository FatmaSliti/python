employee_file = open('employees.txt', 'r')

print(employee_file.readable())
print(employee_file.read())

# read an individual line
print(employee_file.readline())

# readlines takes all lines and put them inside a list 
print(employee_file.readlines())

print(employee_file.readlines()[1]) #to access the first line

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
