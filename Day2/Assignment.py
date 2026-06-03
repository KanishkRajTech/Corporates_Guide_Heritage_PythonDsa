#  Exercise 1
employee_name = "Kanishk Raj"
employee_id = 123
employee_salary = 1000000
employee_department = "Software Engineer"
employee_active_status = True

print(f"Employee Name: {employee_name}")
print(f"Employee ID: {employee_id}")
print(f"Employee Salary: {employee_salary:,.2f}")
print(f"Employee Department: {employee_department}")
print(f"Employee Active Status: {employee_active_status}")

print("variable types")
print(f"type of employee_name : {type(employee_name)}")
print(f"type of employee_id : {type(employee_id)}")
print(f"type of employee_salary : {type(employee_salary)}")
print(f"type of employee_department : {type(employee_department)}")
print(f"type of employee_active_status : {type(employee_active_status)}")

# "Exercise 2"

COMPANY_NAME = "Tech Solutions"
FOUNDING_YEAR = 2015
GST_RATE = 18.0

print(COMPANY_NAME)
print(FOUNDING_YEAR)
print(GST_RATE)
# Exercise 3

age = 21
height = 5.8
name = "Kanishk"
is_student = True
nothing = None

print(age, type(age))
print(height, type(height))
print(name, type(name))
print(is_student, type(is_student))
print(nothing, type(nothing))
# Exercise 4

num_str = "42"
num_int = int(num_str)
num_float = float(num_str)

print("String:", num_str, type(num_str))
print("Integer:", num_int, type(num_int))
print("Float:", num_float, type(num_float))

# Exercise 5

salary = 45000.75
salary_int = int(salary)
salary_str = str(salary)

print("Original:", salary, type(salary))
print("Integer:", salary_int, type(salary_int))
print("String:", salary_str, type(salary_str))


# Exercise 6
full_name = "  John Doe  "

print("Original:", full_name)
print("Strip:", full_name.strip())
print("Upper:", full_name.upper())
print("Lower:", full_name.lower())
print("Length:", len(full_name))


# Exercise 7

emp_code = "HR-EMP-2024"
new_code = emp_code.replace("-", "_")
position = emp_code.find("2024")

print("Original:", emp_code)
print("Updated:", new_code)
print("Position of 2024:", position)


# Exercise 8

name = "Kanishk Raj"
emp_id = 101
department = "Development"
salary = 125000.75
profile = f"""
Employee Profile
----------------
Name       : {name}
ID         : {emp_id}
Department : {department}
Salary     : ₹{salary:,.2f}
"""
print(profile)


# Exercise 9

print(f"{'ID':>6} {'Name':<20}")
print("-" * 30)
print(f"{1:06} {'Kanishk Raj':<20}")
print(f"{2:06} {'Rishu Kumari':<20}")
print(f"{3:06} {'Prince Raj':<20}")



# Exercise 10

name = "Kanishk Raj"
emp_id = "101"
salary = "85000.50"
department = "Software Development"
active_status = True

emp_id = int(emp_id)
salary = float(salary)

print("=" * 40)
print("EMPLOYEE SUMMARY REPORT")
print("=" * 40)
print(f"Name            : {name}")
print(f"Employee ID     : {emp_id}")
print(f"Department      : {department}")
print(f"Salary          : ₹{salary:,.2f}")
print(f"Active Status   : {active_status}")
print("=" * 40)