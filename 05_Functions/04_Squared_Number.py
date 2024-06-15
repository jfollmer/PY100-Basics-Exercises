# Squared Number exercise in the Functions exercises:

"""Write a function that accepts a single argument, a number, and 
returns the result of multiplying its argument by an exponent of 2 (also 
known as squaring the number or raising the number to the power of 2).

squared_number(3)   # 9

"""


def squared_number(n):
    return n**2

print(squared_number(3))


# Given solution also gives another valud solution:

def squared_number(num):
    return num * num

print(squared_number(3))