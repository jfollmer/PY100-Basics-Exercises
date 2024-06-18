# Last Element exercise in Lists exercises:

"""Write a function that returns the last element of a list provided as 
an argument. For example:

print(last(['Earth', 'Moon', 'Mars']))  # Mars

Be sure to handle the case where the input list is empty.
"""


def last(lst):
    return lst.pop() if lst else None

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))

# Alternatively, if you don't want to mutate the list:

def last(lst):
    return lst[-1] if lst else None

print(last(['Earth', 'Moon', 'Mars']))
print(last([]))


# Given solution:

def last(lst):
    if lst:
        return lst[-1]
    else:
        return None