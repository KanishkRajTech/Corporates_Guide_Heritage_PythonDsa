#Section A
# Q 1
# a) Create a list called student_marks with 10 integer values
student_marks = [78, 85, 92, 67, 74, 88, 95, 81, 69, 90]

# b) Print first 3 elements, last 3 elements, and every alternate element
print("First 3 elements:", student_marks[:3])
print("Last 3 elements:", student_marks[-3:])
print("Every alternate element:", student_marks[::2])

# c) Print total number of elements
print("Total number of elements:", len(student_marks))

# d) Update the 5th element to 95
student_marks[4] = 95
print("Updated list:", student_marks)

# e) Print the list in reverse order using slicing
print("Reversed list:", student_marks[::-1])


#Q2
scores = [55, 72, 88, 43, 91, 67, 55, 76]

# a) Append 80
scores.append(80)
print("After append:", scores)

# b) Insert 100 at index 3
scores.insert(3, 100)
print("After insert:", scores)

# c) Remove first occurrence of 55
scores.remove(55)
print("After remove:", scores)

# d) Sort in ascending order
scores.sort()
print("Ascending order:", scores)

# e) Sort in descending order
scores.sort(reverse=True)
print("Descending order:", scores)

# f) Count occurrences of 55 in original list
original_scores = [55, 72, 88, 43, 91, 67, 55, 76]
print("Count of 55:", original_scores.count(55))

# g) Find index of 88
print("Index of 88:", original_scores.index(88))

# h) Pop last element
popped_value = scores.pop()
print("Popped value:", popped_value)
print("Remaining list:", scores)


# Q3 

# a) Squares from 1 to 15
squares = [x**2 for x in range(1, 16)]

# b) Even numbers from 1 to 50
evens = [x for x in range(1, 51) if x % 2 == 0]

# c) Words with more than 4 characters
words = ['hello', 'world', 'python', 'is', 'great']
long_words = [word for word in words if len(word) > 4]

# d) Flatten nested list
matrix = [[1,2,3], [4,5,6], [7,8,9]]
flat_list = [num for row in matrix for num in row]

# e) List of tuples (number, square)
tuples_list = [(x, x**2) for x in range(1, 9)]

print("Squares:", squares)
print("Evens:", evens)
print("Long words:", long_words)
print("Flattened list:", flat_list)
print("Tuples:", tuples_list)


# section B

# Q4
# a) Create a tuple containing all 12 month names
months = (
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
)

# b) Access and print required elements
print("3rd month:", months[2])
print("Last month:", months[-1])
print("Months from index 3 to 6:", months[3:7])

# c) Try to change the first element
try:
    months[0] = "January_New"
except TypeError as e:
    print("Error:", e)

# d) Create a single-element tuple containing your name
name = ("Simran",)
print("Single-element tuple:", name)
print("Type:", type(name))

# e) Convert tuple to list, add 13th month, convert back to tuple
months_list = list(months)
months_list.append("Intercalary")

months = tuple(months_list)

print("Updated tuple:", months)

# Q5
# a) Create and unpack tuple
employee = ('Rajesh Kumar', 34, 'Data Analyst', 75000, 'Bangalore')

name, age, designation, salary, city = employee

print("Name:", name)
print("Age:", age)
print("Designation:", designation)
print("Salary:", salary)
print("City:", city)

# b) Use * operator for unpacking
first, *middle, second_last, last = employee

print("First Item:", first)
print("Middle Items:", middle)
print("Last Two Items:", second_last, last)

# c) Swap values in a single line
x, y, z = 10, 20, 30

x, y, z = z, x, y

print("x =", x)
print("y =", y)
print("z =", z)

# d) Tuple unpacking in a loop
data = [('Alice',90), ('Bob',85), ('Charlie',78), ('Diana',92)]

for name, score in data:
    print(f"{name} scored {score}/100")

# e) Function returning min and max as a tuple
def min_max(numbers):
    return min(numbers), max(numbers)

numbers = [12, 45, 7, 89, 34]

minimum, maximum = min_max(numbers)

print("Minimum:", minimum)
print("Maximum:", maximum)


# Section C
# Q6 
# a) Print each temperature with its index
temperatures = [22, 35, 18, 40, 28, 15, 33, 27]

print("Temperatures with Index:")
for index, temp in enumerate(temperatures):
    print(f"Index {index}: {temp}")

# b) Count temperatures above 30
count = 0
for temp in temperatures:
    if temp > 30:
        count += 1

print("\nTemperatures above 30:", count)

# c) Use zip() to print names and marks
names = ['Alice', 'Bob', 'Charlie']
marks = [85, 92, 78]

print("\nStudent Marks:")
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")

# d) Remove elements until only temperatures above 25 remain
temps = temperatures.copy()

print("\nRemoving temperatures <= 25:")
i = 0
while i < len(temps):
    if temps[i] <= 25:
        removed = temps.pop(i)
        print(f"Removed {removed} -> {temps}")
    else:
        i += 1

print("Final List:", temps)

# e) Multiplication table (1 to 5) as grid
print("\nMultiplication Table (1 to 5):")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()


# section D
# Challenge 1

students = [
    ("Alice",101,[80,85,90,75,88]),
    ("Bob",102,[70,65,75,80,72]),
    ("Charlie",103,[95,92,96,94,90]),
    ("Diana",104,[60,62,58,65,70]),
    ("Ethan",105,[88,85,87,90,89]),
    ("Fiona",106,[76,74,78,80,77]),
    ("George",107,[55,60,58,62,59]),
    ("Helen",108,[91,93,89,90,92]),
    ("Ian",109,[68,70,72,65,69]),
    ("Julia",110,[84,82,86,88,85])
]

def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

averages = [(student[0], calculate_average(student[2])) for student in students]

ranked = sorted(averages, key=lambda x: x[1], reverse=True)

print("\nClass Rank")
for rank, (name, avg) in enumerate(ranked, start=1):
    print(f"{rank}. {name} - {avg:.2f}")

above_75 = sum(1 for _, avg in ranked if avg > 75)
print("Students above 75 average:", above_75)

print("Topper:", ranked[0])
print("Lowest Average:", ranked[-1])



# Challenge 2


inventory = [
    (101,"Laptop",50000,8),
    (102,"Mouse",500,3),
    (103,"Keyboard",1500,4),
    (104,"Monitor",12000,6),
    (105,"Printer",8000,2),
    (106,"Speaker",2500,10),
    (107,"Router",3000,1),
    (108,"Webcam",2000,7)
]

def add_product(product):
    inventory.append(product)

def remove_product(name):
    global inventory
    inventory[:] = [item for item in inventory if item[1] != name]

def update_quantity(name, qty):
    for i, item in enumerate(inventory):
        if item[1] == name:
            inventory[i] = (item[0], item[1], item[2], qty)

def total_inventory_value():
    return sum(price * quantity for _, _, price, quantity in inventory)

print("Total Inventory Value:", total_inventory_value())

print("\nLow Stock Alert")
for product in inventory:
    if product[3] < 5:
        print(product)

print("\nProducts Sorted by Price")
sorted_products = sorted(inventory, key=lambda x: x[2])

for product in sorted_products:
    print(product)

search_name = "Router"

for product in inventory:
    if product[1].lower() == search_name.lower():
        print("\nProduct Found:")
        print(product)
        break
else:
    print("Product not found")