# What's my value? (Part 9) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)


"""The global variable 'a' is initialized in the global scope with a 
value of 7. We then pass it as an argument to my_function, when then
assigns its value to the local variable 'b' and adds 10 to it. The 
global variable remains unaffected due to scope and the immutability of
integer objects. Thus when 'a' is passed to print(), the value 7 is
printed.
"""