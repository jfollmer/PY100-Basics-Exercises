# In the Reading Documentation 1 exercises:

# What happens if we take the list ['fish', 'and', 'chips'] and try to access 
# the element at index position 10? First try to determine what will happen by
# consulting the documentation, then verify your understanding in the Python 
# REPL.


# Standard Library -> Built-in Types -> Sequence Types - list, tuple, range >
#                                       Common Sequence Operations -> Note 8

# This note doesn't explicitly say what happens for both ways off acessing the
# out-of-bounds index position, but it does say that the .index() method 
# raises a ValueError when one isn't found. Testing shows that [] index access
# raises an IndexError.

# Standard Library -> Built-in Exceptions -> Concrete Exceptions -> IndexError

# Searching for "IndexError" specifically reveals this is where it mentions
# this behavior specifically.

print(['fish', 'and', 'chips'][1])
dinner = ['fish', 'and', 'chips']
print(dinner[10])                    # IndexError: list index out of range