# String Formatting exercise in Reading Documentation 2 exercises:

"""Python offers multiple ways to format strings. The str.format method 
is a popular method, but since Python 3.6, a new way called f-strings 
(formatted string literals) was introduced. F-strings offer a concise 
way to embed expressions inside string literals.

Given the following variables:

name = "Victor"
profession = "programmer"

1. How can you print the string "Hello, Victor. You are a programmer." 
using the str.format method? You should fill in the name and profession 
in a string literal that contains the rest of the text.

2. How can you achieve the same result using an f-string?

Refer to the Python documentation on Format String Syntax 
(https://docs.python.org/3/library/string.html#format-string-syntax)
and Formatted string literals
(https://docs.python.org/3/reference/lexical_analysis.html#formatted-string-literals)
for guidance.
"""


name = "Victor"
profession = "programmer"

# 1:
print('Hello, {}. You are a {}.'.format(name, profession))

# 2:
print(f'Hello, {name}. You are a {profession}.')