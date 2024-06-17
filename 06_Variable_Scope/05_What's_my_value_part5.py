# What's my value? (Part 5) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

a = 1

def my_function():
    print(a)
    a = 2

my_function()


"""The global variable 'a' is initialized with the value 1. my_function
passes 'a' to print(), so 1 prints, then 'a' is reassigned with the 
value 2, which we don't capture in any operations in this program, but 
if 'a' were to be used in any other functions, its value will now be 2.
"""


"""I got this wrong: The given solution and testing this indicate that 
because a value is assigned to 'a' within the function, this causes 
variable shadowing, so the global variable 'a' is no longer accessible 
within the function. Therefore, the new local variable 'a' is only 
defined after we try to access it and not before, which causes an error.
"""