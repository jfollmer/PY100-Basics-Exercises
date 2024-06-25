# Arithmetic_Operator_Precedence exercise in Reading Documentation 2 
# exercises:

"""Find the Python Documentation on operator precedence, and use it to 
determine the result of evaluating 4 * 5 + 3**2 / 10.
"""


4 * 5 + 3**2 / 10
4 * 5 + 9 / 10
20 + 0.9
20.9

print(4 * 5 + 3**2 / 10)    # to check

"""The relevant order for this code:

**      exponentiation
*, /    multiplication and division
+       addition

https://docs.python.org/3/reference/expressions.html#operator-precedence
"""