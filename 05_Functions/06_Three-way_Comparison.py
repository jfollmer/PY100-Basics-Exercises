# Three-way Comparison exercise in the Functions exercises:

"""Write a function that compares the length of two strings. It should 
return -1 if the first string is shorter, 1 if the second string is 
shorter, and 0 if they're of equal length. For example:

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

"""


def compare_by_length(string1, string2):
    if len(string1) < len(string2):
        return -1
    elif len(string1) > len(string2):
        return 1
    else:
        return 0
    
print(compare_by_length('patience', 'perseverance'))
print(compare_by_length('strength', 'dignity'))
print(compare_by_length('humor', 'grace'))


"""The given solution explains that: 'This kind of comparison, where you 
compare two values using <, >, and == (== is implicit here), is called a 
three-way comparison. Such comparisons are useful in sorting algorithms 
to determine how values are sorted.
"""