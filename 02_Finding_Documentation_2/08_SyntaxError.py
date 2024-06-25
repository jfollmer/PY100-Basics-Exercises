# SyntaxError exercise in Reading Documentation 2 exercises:

"""The following code raises a SyntaxError:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')

What does a SyntaxError indicate? Try running the above code, then use 
the resulting error message to fix the error.       
"""


speed_limit = 60
current_speed = 80

if current_speed > speed_limit:                         # added colon
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')
    
"""
  File "filpath", line 20
    if current_speed > speed_limit
                                  ^
SyntaxError: expected ':'

A SyntaxError is raised when the parser encounters a syntax error.

https://docs.python.org/3/library/exceptions.html#SyntaxError
"""