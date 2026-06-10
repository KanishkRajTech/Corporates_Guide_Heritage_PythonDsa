#fore loops with list

# Basic for loop
colors = ['red', 'green', 'blue']
for color in colors:
    print(color)

# Loop with index using enumerate()
for i, color in enumerate(colors):
    print(f'Index {i}: {color}')

# Loop with range() (index-based access)
for i in range(len(colors)):
    print(colors[i])

# Modifying a list while iterating (use index or copy)
nums = [1, 2, 3, 4, 5]
for i in range(len(nums)):
    nums[i] *= 2        # Double each value
print(nums)    # [2, 4, 6, 8, 10]



# while loops with list
stack = [10, 20, 30, 40]

while stack:           # Loop until list is empty
    item = stack.pop()
    print(item)        # 40, 30, 20, 10

# While loop with index
nums = [5, 10, 15, 20]
i = 0
while i < len(nums):
    print(nums[i])
    i += 1




