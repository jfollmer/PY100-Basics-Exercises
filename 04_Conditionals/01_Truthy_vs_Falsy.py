# Exercise 1 in the Conditionals exercises:

"""Without looking at your notes or the official documentation, try to 
recall all values that count as falsy in Python.
"""


# 0
# None
# False
# Empty collections
# Empty strings


"""Given solution specifies the individual types of collections (it left
out frozenset() though, and even the official documentation omits this) 
and expands on 0 values to include other numeric type representations of 
0. It also mentions how to test this with the bool() constructor:
"""

print(bool(set()))
print(bool(frozenset()))

"""It also mentions how custom classes can define their own falsy 
values.
"""