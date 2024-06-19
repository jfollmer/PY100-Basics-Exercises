# Reading Error Messages exercise in Debugging exercises:

"""You come across the following code. What errors does it raise for the 
given examples and what exactly do the error messages mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

print(find_first_nonzero_among(0, 0, 1, 0, 2, 0))
print(find_first_nonzero_among(1))

"""


def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

print(find_first_nonzero_among([0, 0, 1, 0, 2, 0]))    # added []
print(find_first_nonzero_among([1]))     # added []

"""
Traceback (most recent call last):
  File "filepath" line 11, in <module>
    find_first_nonzero_among(0, 0, 1, 0, 2, 0)
TypeError: find_first_nonzero_among() takes 1 positional argument but 
 6 were given

The TypeError error occurs in line 11. This error is raised because 
find_first_nonzero_among(numbers) is expecting a single iterable as an
argument. If you were to wrap the arguments in line 11 to a list or 
other collection literal, this would work. Once you fix that, however, 
two more errors occur:

Traceback (most recent call last):
  File "filepath", line 12, in <module>
    find_first_nonzero_among(1)
  File "filepath", line 7, in find_first_nonzero_among
    for n in numbers:
TypeError: 'int' object is not iterable

The TypeError is due to the combination of lines 12 and 7. On line 12 we
call the function and pass an integer as the argument, but once inside 
the function, the for loop on line 7 requires an iterable, and an 
integer isn't iterable. Again, we could wrap the argument in a list or
other collection literal.
"""