# What's my value? (Part 9) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)


"""A list is assigned to the variable 'b' in the global scope. 
my_function then accesses the first element and reassigns it with a 
value of 10. Since lists are mutable objects, the global variable
reflects this change. Thus when 'b' is passed to print(), the modified
list [10, 2, 3] is printed.
"""


"""The given solution uses the phrase 'indexed reassignment is a 
mutating action'.
"""