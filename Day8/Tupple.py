# Tuples


# Empty tuple
empty = ()

# Single-element tuple  (NOTE: trailing comma is REQUIRED)
single = (42,)      # This IS a tuple
not_tuple = (42)    # This is just the integer 42!

# Tuple of integers
coords = (10, 20, 30)

# Mixed types
person = ('Alice', 25, 'Engineer', True)

# Tuple without parentheses (tuple packing)
point = 3, 5, 7     # (3, 5, 7)

# Using tuple() constructor
from_list = tuple([1, 2, 3])    # (1, 2, 3)
from_str  = tuple('hello')      # ('h', 'e', 'l', 'l', 'o')



# Tuples are immutable
coords = (10, 20, 30)
# coords[0] = 99    -> TypeError: 'tuple' object does not support item assignment
# coords.append(40) -> AttributeError: 'tuple' object has no attribute 'append'

# However, if a tuple contains a mutable object (like a list), that object CAN change:
t = (1, [2, 3], 4)
t[1].append(99)      # The list inside the tuple is modified
print(t)             # (1, [2, 3, 99], 4)  <- tuple structure unchanged


#Tupple use case
# Function returning multiple values (actually a tuple)
def get_dimensions():
    return 1920, 1080    # Returns (1920, 1080)

width, height = get_dimensions()
print(width, height)  # 1920 1080

# Tuple as dictionary key
locations = {}
locations[(28.6139, 77.2090)] = 'New Delhi'
locations[(19.0760, 72.8777)] = 'Mumbai'

# Named tuple for structured records
from collections import namedtuple
Employee = namedtuple('Employee', ['name', 'age', 'dept'])
emp = Employee('Ravi', 30, 'IT')
print(emp.name, emp.dept)   # Ravi  IT




#Tupple unpacking
# Basic unpacking
point = (3, 7)
x, y = point
print(x, y)   # 3  7

# Unpacking with more elements
person = ('Alice', 28, 'Mumbai', 'Engineer')
name, age, city, role = person
print(name, age)   # Alice 28

# Using underscore _ to ignore values
_, age, _, role = person
print(age, role)   # 28  Engineer

# Extended unpacking with * (star operator)
first, *rest = [1, 2, 3, 4, 5]
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

*start, last = [10, 20, 30, 40]
print(start)   # [10, 20, 30]
print(last)    # 40

a, *middle, z = (1, 2, 3, 4, 5)
print(middle)  # [2, 3, 4]


#swapping values using unpaking

# Traditional swap (requires temp variable)
a, b = 10, 20
temp = a
a = b
b = temp
print(a, b)   # 20  10

# Pythonic swap (tuple unpacking)
a, b = 10, 20
a, b = b, a
print(a, b)   # 20  10

# Multi-variable swap
x, y, z = 1, 2, 3
x, y, z = z, x, y
print(x, y, z)   # 3  1  2

# Swap works with any data type
s1, s2 = 'hello', 'world'
s1, s2 = s2, s1
print(s1, s2)   # world  hello


#unpaking loop

# Iterating over list of tuples
students = [('Alice', 90), ('Bob', 85), ('Charlie', 78)]

for name, score in students:
    print(f'{name} scored {score}')

# Using enumerate() for index + value
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
# Output: 0: apple  /  1: banana  /  2: cherry

# Using zip() to iterate two lists simultaneously
names  = ['Alice', 'Bob', 'Charlie']
scores = [90, 85, 78]
for name, score in zip(names, scores):
    print(f'{name}: {score}')




