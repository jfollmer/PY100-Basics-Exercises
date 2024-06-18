# First Element exercise in Lists exercises:

"""Write a function that returns the first element of a list provided 
as an argument. For example:

print(first(['Earth', 'Moon', 'Mars']))  # Earth

Be sure to handle the case where the input list is empty.
"""


def first(my_list):
    return my_list[0] if my_list else "List is empty."
    
print(first(['Earth', 'Moon', 'Mars']))
print(first([]))


# Given solution:

def first(lst):
    if lst:
        return lst[0]
    else:
        return None