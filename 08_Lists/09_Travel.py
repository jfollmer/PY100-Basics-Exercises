# Travel exercise in Lists exercises:

# The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

"""Write a function that, without using the built-in in operator, checks 
whether a specific destination is included within destinations. For 
example: When checking whether 'Barcelona' is contained in destinations, 
the expected output is True, whereas the expected output for 'Nashville' 
is False.

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

"""


def contains(item, lst):
    for i in lst:
        if i == item:
            print(True)
            return
        else:
            continue
    print(False)
    return


contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False


"""The given solution doesn't contain the print() statements, but I 
included them since the function fall examples for expected output 
weren't inside print() statements. (And I guess the style is to not 
include the else: continue block for something so simple?)

It mentions that using the 'in' in the for loop is not the 'in' 
operator, just part of the syntax of the for statement.
"""

def contains(element, lst):
    for item in lst:
        if item == element:
            return True

    return False

# A while loop solution is also given if you want to avoid 'in' 
# altogether:

def contains(element, lst):
    index = 0
    while index < len(lst):
        if lst[index] == element:
            return True

        index += 1

    return False

# And an error-checking solution using the 'in' operator:

def contains(element, lst):
    return element in lst