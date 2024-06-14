# Exercise 7 in the Loops exercises:

"""Take a moment to read the Python documentation on the continue 
statement.

Write a for loop that iterates over the elements of the list cities and 
prints the length of each string. If the element is None, use the 
continue statement to skip forward to the next iteration without 
printing anything.
"""

cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]


# https://docs.python.org/3/reference/simple_stmts.html#grammar-token-python-grammar-continue_stmt
# "It continues with the next cycle of the nearest enclosing loop."

for city in cities:
    if city == None:
        continue
    print(len(city))


# As mentioned in the given solution, could have also used pass here
# (but I think continue is cleaner):

for city in cities:
    if city == None:
        pass
    else:
        print(len(city))
