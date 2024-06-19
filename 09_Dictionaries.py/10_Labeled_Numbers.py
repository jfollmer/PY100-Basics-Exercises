# Labeled Numbers exercise in Dictionaries exercises:

"""Use a for loop to iterate over the numbers dictionary and print each 
element's key/value pair.

numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

Expected Output:

A high number is 100.
A medium number is 50.
A low number is 10.

"""


numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

for (key, value) in numbers.items():
    print(f'A {key} number is {value}')


# The given solution doesn't use the parentheses:

for key, value in numbers.items():
    print(f"A {key} number is {value}.")