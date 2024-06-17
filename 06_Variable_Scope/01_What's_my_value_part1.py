# What's my value? (Part 1) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

if True:
    my_value = 20

print(my_value)


# my_value is defined within a loop and not within a function, so line 9
# should print 20. (And it does.)



"""The given solution mentions that a variable initialized inside any 
block that's not inside a function is accessible outside of the block,
not just inside loops.
"""

# What do you think will happen if we run the following code instead:

if False:
    my_new_value = 42

print(my_new_value)


"""Since the condition of the if statement is always False, so nothing 
within the block executes, meaning the variable my_new_value is never
initialized. When we pass this identifier to print(), it should raise a 
NameError.
"""