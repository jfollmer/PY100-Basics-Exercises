# Is Empty? exercise in Strings exercises:

"""Write a function that checks whether a string is empty or not. For 
example:

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

"""


def is_empty(string):
    return True if not string else False    # you can eliminate the
                                            # 'True if' and 'else False'
                                            # as seen in solution
                                            
print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True


# Given solutions:

def is_empty(s):
    return s == ''

def is_empty(s):
    return len(s) == 0

def is_empty(s):
    return not s    # More Pythonic to leverage the fact that an empty
                    # string is falsy, which is a built-in feature of
                    # the language.