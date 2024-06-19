# What Color? exercise in Dictionaries exercises:

# Using the following code, select and print the value 'blue' from the 
# car object:

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}


print(car['color'])


# Given solution also mentions dict.get(key, default_value):

print(car.get('mileage', 0))