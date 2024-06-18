# Type exercise in Lists exercises:

# How can you check if a variable holds a value that is a list? Given 
# two variables, verify whether the values they hold are lists.

some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'


print('list' if type(some_value1) == list else 'not a list')
print('list' if type(some_value2) == list else 'not a list')


# Given solution uses a built-in function (documentation here:
# https://docs.python.org/3/library/functions.html#isinstance):

isinstance(some_value1, list)  # True
isinstance(some_value2, list)  # False