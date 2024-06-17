# What's my value? (Part 7) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)


"""Variable 'a' is initialized in the global scope with the value 1. 
Then in my_function, we use the global keyword to be able to use the 
global 'a' within the function. 'a' is then reasigned with the value 2, 
which occurs when the function is called on line 12. So when 'a' is 
passed to print() on line 13, its new value of 2 is printed.
"""