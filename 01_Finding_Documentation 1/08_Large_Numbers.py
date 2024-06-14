# In the Reading Documentation 1 exercises:

# Using the Python documentation, determine how you can write large numbers in 
# a way that makes them easier to read.


# Searching for "number underscore", the website indicates PEP 515, which 
# explains in some detail. But this is isn't explicitly said anywhere else. 
# Implied here:

# Standard Library -> Other Built-in Types -> Integer string conversion length 
#                                                                   limitation

# And this, provided in the solution, explains that "underscores are now 
# allowed for grouping purposes in literals":

# The Python Language Reference -> 2. Lexical Analysis -> 
#                                                       2.4.5 Integer Literals


# Further Exploration: Is it okay to write 1_987_654_321 as 19_87_65_4321?

# Yes, as described in PEP 515. To test:

print(type(19_87_654321))  # <class 'int'>