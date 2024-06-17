# What's my value? (Part 4) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

a = 1

def my_function():
    print(a)

my_function()


"""The global variable 'a' is accessible inside of functions, so 
my_function is able to pass 'a' to print() within it, so its value 1
prints.
"""