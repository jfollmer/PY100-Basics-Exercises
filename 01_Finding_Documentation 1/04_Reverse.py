# In the Reading Documentation 1 exercises:

# Is there a method to reverse a string, for example turning 'hello' into 
# 'olleh'?


# Standard Library -> Built-in Types -> Text Sequence Types - str -> 
#                                                               String Methods

# No, there's nothing built-in that does this. There's a list.reverse() method,
# but not a str.reverse() method. But you can do with with a string slice:

string = 'hello'
print(string[::-1])     # olleh