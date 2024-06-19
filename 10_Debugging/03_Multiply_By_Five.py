# Multiply By Five exercise in Debugging exercises:

"""When the user inputs 10, we expect the program to print The result is 
50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

"""


def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = int(input())    # added int()

print(f"The result is {multiply_by_five(number)}!")

"""If your input is '3', this prints 'The result is 33333!' The input()
funtion always returns the input as a string, so you have to perform 
type coercion if you want to use the input as an integer or any other 
type. Since we didn't do that, it multiplies a string by an integer, 
and it performs string concatenation. 
"""