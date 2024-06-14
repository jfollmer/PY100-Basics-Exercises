# Exercise 6 in the Loops exercises:

"""Your friends just showed up! Given the following list of names, use a 
for loop to greet each friend individually.
"""

friends = ['Sarah', 'John', 'Hannah', 'Dave']

"""Expected output:

Hello, Sarah!
Hello, John!
Hello, Hannah!
Hello, Dave!
"""


for name in friends:
    print(f'Hello, {name}!')


"""The given solution mentions a convention: "When naming variables in a
for loop, it's commonplace to use a singular-plural format: for friend 
in friends, for cat in cats, etc. This convention makes the code more 
readable and clearly indicates the relationship between the iterable and 
the loop variable."
"""

for friend in friends:
    print(f'Hello, {friend}!')