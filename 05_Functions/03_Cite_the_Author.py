# Cite the Author exercise in the Functions exercises:

"""Let's generalize the function from the previous exercise. Implement a 
function named cite that takes two string arguments: the author of the 
quote and what they said. It then prints the quote, as shown below.

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

"""

def cite(author, quote):
    print(f'{author} said: "{quote}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')


"""The given solution provides another way to do this using the
str.format() method (but mentions in the video that the most common and 
preferred way is to use f-strings):
"""

def cite(author, quote):
    print('{} said: "{}"'.format(author, quote))

cite('Bruce Eckel', 'Python is executable pseudocode.')

"""Documentation for the str.format() method:
'The string on which this method is called can contain literal text or 
replacement fields delimited by braces {}. Each replacement field 
contains either the numeric index of a positional argument, or the name 
of a keyword argument. Returns a copy of the string where each 
replacement field is replaced with the string value of the corresponding 
argument.'
"""