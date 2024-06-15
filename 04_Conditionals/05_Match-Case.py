# Match-Case exercise in the Conditionals exercises:

"""Examine the code shown below. Without running it, determine what it 
will print. If you're not sure, refer to our Python book.
"""

animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')


"""This defines mutliple match cases. animal = 'horse', so it's tested
against each case for value equality. It matches the third case, so line
15 prints and the reset of the block is skipped.
"""