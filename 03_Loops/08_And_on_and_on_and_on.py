# Exercise 8 in the Loops exercises:

"""The following code keeps looping forever. (You can hit Ctrl-C to stop 
it.) Why does the loop keep running? Modify it so that it stops after 
the first iteration.

while True:
    print("and on")

"""


"""It keeps running because the while loop need some code that 
eventually changes the while condition to False (or a break statement to
break the loop) otherwise the condition remains True and the loop keeps 
running.
"""

while True:
    print("and on")
    break