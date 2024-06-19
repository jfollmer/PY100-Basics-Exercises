# Multiple Cars exercise in Dictionaries exercises:

"""Create a nested dictionary that contains the following data.

Car

type	color	year
sedan	blue	2003

Truck

type	color	year
pickup	red	    1998

"""


vehicles = {
    'car': {
        'type': 'sedan', 
        'color': 'blue', 
        'year': 2003,
    },
    'truck': {
        'type': 'pickup', 
        'color': 'red', 
        'year': 1998,
    },
    
}


# Given solution uses print() statements to test that it was constructed
# properly:

print(vehicles['car'])
print(vehicles['car']['year'])