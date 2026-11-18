#1. Take input from the user and print the data type immediately

name = input("Enter Employee Name: ")
print("Data type:", type(name))

# Convert ID to a whole number (integer)
empid = int(input("Enter Employee ID:"))
print("Data type:", type (empid))

# Convert Salary to a decimal number 
salary= float(input("Enter salary:"))
print("Data type:", type (salary))

Department= input("Enter department:")
print("Data type:", type (Department))

# Read active status as string first 
activeinput = input("Is the employee active? (yes/no): ")

# Convert the string answer to a boolean value (TRUE/FALSE)
#If the user enters 'yes', it becomes True. Otherwise, it becomes False.
is_active = (activeinput.lower() =="yes")
print("Data type:", type(is_active))
