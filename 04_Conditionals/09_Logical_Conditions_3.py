# Logical Conditions 2 exercise in the Conditionals exercises:

# Without running the following code, determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")


"""Since sale = True, line 6 uses the not operator, which returns True 
for a falsy value or False for a truthy value. The ternary expression
then evaluates as 3.99, which on line 8 is passed to the f-string, which 
is passed to the print statement, so $3.99 prints.
"""