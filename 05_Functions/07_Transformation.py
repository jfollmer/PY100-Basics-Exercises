# Transformation exercise in the Functions exercises:

"""Use Python's string methods on the string 'Captain Ruby' to create a 
string with the value 'Captain Python'.
"""



# A solution that doesn't use methods:

old_string = 'Captain Ruby'
new_string = old_string[0:8] + 'Python'

print(new_string)

# Another solution using a method:

words = old_string.split
new_string = old_string.split()[0] + ' Python'

print(new_string)

# Best solution using a method:

new_string = old_string.replace('Ruby', 'Python')

print(new_string)


"""Given solutions don't assign variables, just call the methods
directly on the string (they happen to include both of the less elegant
solutions I tried first, cool) and the one that uses string slicing has 
better notation:
"""

'Captain Ruby'.replace('Ruby', 'Python')
'Captain Ruby'[:8] + 'Python'
'Captain Ruby'.split(' ')[0] + ' Python'