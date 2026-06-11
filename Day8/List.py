# Empty list
empty_list = [] #square brackets.

# List of integers
numbers = [10, 20, 30, 40, 50]

# List of strings
fruits = ['apple', 'banana', 'cherry']

# Mixed data types
mixed = [1, 'hello', 3.14, True, None]

# Nested list (list inside list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using list() constructor
from_range = list(range(1, 6))   
from_string = list('hello')      

# indexing 
fruits = ['apple', 'banana', 'cherry', 'mango', 'grape']

print(fruits[0])    
print(fruits[2])    
print(fruits[-1])   
print(fruits[-2])  

# Modifying an element using index
fruits[1] = 'blueberry'
print(fruits)       


# Sliceing 
nums = [0, 10, 20,30, 40, 50, 60, 70, 80, 90]

print(nums[2:5])     # [20, 30, 40]   (index 2,3,4)
print(nums[:4])      # [0, 10, 20, 30]  (from start to index 3)
print(nums[6:])      # [60, 70, 80, 90] (from index 6 to end)
print(nums[::2])     # [0, 20, 40, 60, 80] (every 2nd item)
print(nums[::-1])    # [90, 80, 70, ...0]  (reversed list)
print(nums[1:8:3])   # [10, 40, 70]  (start=1, stop=8, step=3)

# Slicing does NOT modify the original list
sub = nums[2:5]
print(sub)           # [20, 30, 40]


# Appand
colors = ['red', 'green', 'blue']

colors.append('yellow')
print(colors)   # ['red', 'green', 'blue', 'yellow']

# Appending different data types
colors.append(100)      # ['red', 'green', 'blue', 'yellow', 100]
colors.append([1, 2])   # Appends as a single nested list
print(colors)   # ['red', 'green', 'blue', 'yellow', 100, [1, 2]]


# Common use: building a list dynamically with a loop
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(squares)   # [1, 4, 9, 16, 25]


animals = ['cat', 'dog', 'cat', 'rabbit', 'dog']

animals.remove('cat')      # Removes FIRST 'cat' only
print(animals)  # ['dog', 'cat', 'rabbit', 'dog']

# Safe removal using 'in' check
if 'rabbit' in animals:
    animals.remove('rabbit')

# remove() raises ValueError for missing item:
# animals.remove('elephant')   -> ValueError: list.remove(x): x not in list


#Short
nums = [5, 2, 8, 1, 9, 3]

nums.sort()                   # Ascending
print(nums)   # [1, 2, 3, 5, 8, 9]

nums.sort(reverse=True)       # Descending
print(nums)   # [9, 8, 5, 3, 2, 1]

# Sort strings alphabetically
words = ['banana', 'apple', 'cherry', 'date']
words.sort()
print(words)  # ['apple', 'banana', 'cherry', 'date']

# Sort by length using key parameter
words.sort(key=len)
print(words)  # ['date', 'apple', 'banana', 'cherry']

# sorted() returns a NEW sorted list (original unchanged)
original = [4, 1, 3, 2]
new_sorted = sorted(original)
print(original)    # [4, 1, 3, 2]  <- unchanged
print(new_sorted)  # [1, 2, 3, 4]


# Reverse
items = [1, 2, 3, 4, 5]

items.reverse()
print(items)    # [5, 4, 3, 2, 1]

# reversed() returns an iterator (does not modify original)
nums = [10, 20, 30]
for x in reversed(nums):
    print(x)   # 30, 20, 10

# Tip: slicing [::-1] also reverses but creates a NEW list
rev_copy = nums[::-1]   # [30, 20, 10]  (original unchanged)

