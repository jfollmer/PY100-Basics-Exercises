# Argument Signatures exercise in Reading Documentation 2 exercises:

"""How many arguments does the str.join method expect? What happens if 
you call it with fewer or more arguments?
"""


"""It expects one argument, an iterable. It raises a TypeError if there 
are too many/few arguments, or if there are any non-string values in the
iterable.

https://docs.python.org/3/library/stdtypes.html#str.join
"""
