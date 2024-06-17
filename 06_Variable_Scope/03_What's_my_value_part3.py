# What's my value? (Part 3) exercise in Variable Scope exercises:

# What will the following code do and why? Don't run it until you have 
# tried to answer.

def my_function():
    a = 1

    if True:
        print(a)

my_function()


"""The local variable 'a' is initialized within my_function and is 
passed to print() within this function, so its value 1 prints when the 
function is called, and the variable is deleted when the function
finishes executing.
"""


"""The given solution mentions that variables initialized in the same 
scope where a block begins can be accessed inside the block, which seems 
like another way of saying what I said, but maybe blocks are worth 
mentioning in addition to functions.
"""


"""My modified answer: The local variable 'a' is initialized within 
my_function and is passed to print() within a code block within this 
function, so its value 1 prints when the function is called, and the 
variable is deleted when the function finishes executing.
"""