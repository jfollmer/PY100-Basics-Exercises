# Check Prefix exercise in Strings exercises:

"""Write a function that checks whether a string starts with a specific 
prefix.

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

"""


def starts_with(string, prefix):
    return string.find(prefix) == 0

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True


# Given solution uses str.startswith() method, which I'd forgotten 
# about:

def starts_with(string, prefix):
    return string.startswith(prefix)