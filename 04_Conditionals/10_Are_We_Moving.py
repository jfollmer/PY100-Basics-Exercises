# Are we moving? exercise in the Conditionals exercises:

"""Determine what the following code snippet prints. First solve it in 
your head or on paper, then run it in your Python environment to check 
the result.
"""

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

"""Bonus question: Do we need the parentheses in the boolean expression 
or could we have written the following?:
"""

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0


# My solution:

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
# = True and (speed > 0 or acceleration > 0)
# = True and (False or True)
# = True and True
print(is_moving)    # prints True

# Bonus:

is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
# = True and speed > 0 or acceleration > 0
# = True and False (False is returned and the rest is short-circuited)

"""No. The parentheses are required to prevent the final portion from
being short-circuited.
"""