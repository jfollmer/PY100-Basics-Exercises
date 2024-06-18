# Vocabulary exercise in Lists exercises:

"""You've been given a list of vocabulary words grouped into sub-lists, 
by meaning. This is a two-dimensional list or a nested list. Write some 
code that iterates through and prints all the words, one per line.
"""

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...


for group in vocabulary:
    for word in group:
        print(word)


# Given solution has a better variable name for the nested lists:

for synonyms in vocabulary:
    for word in synonyms:
        print(word)