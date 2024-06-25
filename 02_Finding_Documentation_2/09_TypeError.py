# TypeError exercise in Reading Documentation 2 exercises:

"""The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

What does a TypeError indicate? Try running the above code, then use the 
resulting error message to determine exactly what is wrong. (You don't 
have to fix this code.)
"""


tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

"""
  File "filepath", line 23, in <module>
    length_of_tweet = len(tweet + 5)
                          ~~~~~~^~~
TypeError: can only concatenate str (not "int") to str

A TypeError is raised when an operation or function is applied to an 
object of inappropriate type.

https://docs.python.org/3/library/exceptions.html#TypeError
"""