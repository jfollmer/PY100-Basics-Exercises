# Is Empty or Blank? exercise in Strings exercises:

"""Write an is_empty_or_blank function to determine whether a string is 
either empty or consists entirely of spaces. For example:

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

"""


def is_empty_or_blank(string):
    return not string or string.isspace()   # seen in several student
                                            # solutions too

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True


# Given solutions use the str.strip() method, but str.isspace() seems
# more comprehensive to me:

def is_empty_or_blank(s):
    return s.strip(' ') == ''

def is_empty_or_blank(s):
    return len(s.strip(' ')) == 0

def is_empty_or_blank(s):
    return not s.strip(' ')