# In the Reading Documentation 1 exercises:

# Use the Python documentation for the str class to determine which method can 
# be used to right justify a str object.


# Standard Library -> Built-in Types -> Text Sequence Types - str -> 
#                                                               String Methods

# str.rjust(width [, fillchar])

# Return a new string, right-justified with a given width.
# Default fillchar is an ASCII space, or can specify.
# If width <= len(str), original string is returned.

string = "random string"
print(string.rjust(37, '\\'))
# \\\\\\\\\\\\\\\\\\\\\\\\random string