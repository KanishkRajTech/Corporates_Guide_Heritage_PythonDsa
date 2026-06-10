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
