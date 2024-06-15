# Locale Part 1 exercise in the Functions exercises:

"""Write a function that extracts the language code from a locale
(https://en.wikipedia.org/wiki/Locale_(computer_software). A locale is a
combination of a language code, a region, and usually also a character 
set, e.g en_US.UTF-8.

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

"""

def extract_language(locale):
    return locale[:2]

print(extract_language('en_US.UTF-8'))
print(extract_language('en_GB.UTF-8'))
print(extract_language('ko_KR.UTF-16'))

# Given solution uses the str.split() method with index access:

def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko