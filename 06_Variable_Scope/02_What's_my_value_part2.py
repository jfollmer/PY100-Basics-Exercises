# What's my value? (Part 2) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()


"""Since x is initialized in the global scope, it is accessible inside
any functions, and my_function is able to perform reassignment on it.
This prints 15."""