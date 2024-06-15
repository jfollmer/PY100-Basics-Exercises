# Check the Weather exercise in the Conditionals exercises:

"""Take your code from the previous Check the Weather exercise and 
rewrite it as a match-case statement. Feel free to add more cases 
besides 'sunny' and 'rainy'.
"""


import random

weather = random.choice([       
    'sunny', 
    'rainy', 
    'cloudy',
    'windy', 
    'snowy',
    'hurricane',
    'tornado',
])

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case 'cloudy':
        print("Don't need sunglasses today.")
    case 'windy':
        print("Let's go sailing!")
    case 'snowy':
        print("Get the shovel ready.")
    case 'hurricane':
        print("Evacuate!")
    case 'tornado':
        print("Shelter in place!")
    case _:
        print("Let's stay inside.")

"""Fun to try out something from the random module we looked at in 
ex. 'Yes? or No? Part 1' to test this with. Nice to see a couple other 
students did this too.
"""