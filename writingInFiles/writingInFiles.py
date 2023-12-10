# employee_file = open('employees.txt', 'a') # a stands for append(add to the end)

# # employee_file.write('Toby - Human Resources')
# employee_file.write('\nFatma - Web Developer')


employee_file = open('employees1.txt', 'w') # w stands for write
#with write, unlike append, it overrides all the file 

employee_file.write('\nFatmaa - Web Developer')

employee_file2 = open('index.html', 'w')
employee_file2.write('<p>This is HTML</p>')

employee_file.close()
