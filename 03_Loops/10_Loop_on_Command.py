# Exercise 9 in the Loops exercises:

"""Modify the following code so the loop continues iterating until the 
user inputs 'yes'.

while True:
    print('Should I stop looping?')
    answer = input()

"""


while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break


# Given solution suggests to prompt the user for the "right" answer
# (comment out whichever version you're not testing):


while True:
    print('Should I stop looping?')
    answer = input()
    if answer == 'yes':
        break
    print('Incorrect answer. Please answer "yes".')


"""Although I think you could also handle this by altering the code to
accept other versions of "yes", such as the following, maybe in addition
to prompting:
"""

while True:
    print('Should I stop looping?')
    answer = input()
    if answer.lower() == 'yes' or answer.lower() == 'y':
        break
    print('If you want me to stop looping, enter "yes" or "y".')