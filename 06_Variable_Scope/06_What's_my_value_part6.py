# What's my value? (Part 6) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

a = 1

def my_function():
    a = 2

my_function()
print(a)


"""The global variable 'a' is initialized with the value 1, but a 
separate local variable 'a' is initialized with the value 2 when 
my_function is called on line 11, causing variable shadowing, and we 
don't do anything with this variable. The global 'a' remains unchanged. 
Passing 'a' to print() on line 12 uses the global variable, so the value 
1 prints.
"""