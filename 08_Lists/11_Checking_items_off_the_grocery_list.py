# Checking items off the grocery list exercise in Lists exercises:

"""We have a grocery list. As we check off items on that list, we want 
to remove them from the list.

Write code that removes the items from grocery_list, one by one, until 
it is empty. If you print the elements you remove, the expected behavior 
would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

# Your code.

print(grocery_list)

Expected output:

paprika
tofu
garlic
quinoa
carrots
broccoli
hummus
[]

"""

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 
                'carrots', 'broccoli', 'hummus']

for num in range(len(grocery_list)):
    print(grocery_list.pop(0))

print(grocery_list)


# Given solution uses a while loop. It's a common pattern to use the
# truthiness of a list if we're trying to remove all the items from it:

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    checked_item = grocery_list.pop(0)
    print(checked_item)

print(grocery_list)

"""It also mentions that you can't mutate an iterable while you're
iterating over it, because moving elements around while you're iterating
can cause some strange behavior, which I encountered the with my first
attempt at a solution:
"""

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 
                'carrots', 'broccoli', 'hummus']

for item in grocery_list:
    print(item)
    grocery_list.remove(item)

print(grocery_list)

# paprika
# garlic
# carrots
# hummus
# ['tofu', 'quinoa', 'broccoli']


# My attempt had been:

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa', 
                'carrots', 'broccoli', 'hummus']

for item in grocery_list:
    print(grocery_list.pop(0))

print(grocery_list)

# paprika
# tofu
# garlic
# quinoa
# ['carrots', 'broccoli', 'hummus']