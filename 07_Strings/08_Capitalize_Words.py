# Capitalize Words exercise in Strings exercises:

"""Write code that capitalizes the words in the string 'launch school 
tech & talk', so that you get the string 'Launch School Tech & Talk'.
"""


string = 'launch school tech & talk'
print(string.title())


"""The given solution writes a whole function, and also provides another
solution that doesn't use the str.title() method but rather str.split(), 
lst.append(), str.capitalize(), and str.join():
"""

def capitalize_words(string):
    return string.title()

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk


def capitalize_words(string):
    words = string.split(' ')
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())

    return ' '.join(capitalized_words)

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk