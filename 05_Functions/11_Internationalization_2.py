# Internationalization 2 exercise in the Functions exercises:

"""Building on your solutions from the previous exercises, write a 
function local_greet that takes a locale as input, and returns a 
greeting. The locale lets us greet people from different countries 
appropriately, even when they share a common language, for example:

print(local_greet('en_US.UTF-8'))       # Hey
print(local_greet('en_GB.UTF-8'))       # Hello
print(local_greet('en_AU.UTF-8'))       # Howdy

Distinguish greetings for English speaking countries like the US, UK, 
Canada, or Australia in your implementation, and feel free to fall back 
on the language-specific greetings in all other cases, for example:

print(local_greet('fr_FR.UTF-8'))       # Salut
print(local_greet('fr_CA.UTF-8'))       # Salut
print(local_greet('fr_MA.UTF-8'))       # Salut

When implementing local_greet, make sure you re-use your 
extract_language, extract_region, and greet functions from the previous
exercises.
"""

def extract_language(locale):
    return locale[:2]

def extract_region(locale):
    return locale[3:5]

def greet(language_code):
    match language_code:
        case 'en':              # English
            return 'Hi!'
        case 'fr':              # Français (French)
            return 'Salut!'
        case 'pt':              # Português (Portuguese)
            return 'Olá!'
        case 'de':              # Deutch (German)
            return 'Hallo!'
        case 'sv':              # Svenska (Swedish)
            return 'Hej!'
        case 'af':              # Afrikaans
            return 'Haai!'
        case 'it':              # Italiano (Italian)
            return 'Salve!'
        case 'es':              # Español (Spanish)
            return 'Hola!'
        case 'ja':              # 日本語 (Japanese)
            return 'こんにちは!'
        case 'zh':              # 中文 (Chinese (Mandarin))
            return '你好!'
        case 'uk':              # Українська Мова (Ukrainian)
            return 'Привіт!'
        case _:
            return 'This language is not currently supported.'

def local_greet(locale):
    language_code = extract_language(locale)
    region = extract_region(locale)
    greeting = greet(language_code)
    match language_code:
        case 'en': 
            match region:
                case 'US':
                    return 'Hey!'
                case 'UK':
                    return greeting
                case 'AU':
                    return 'Howdy!'
                case _:
                    return greeting
        case _:
            return greeting

print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))
print(local_greet('ru_RU.UTF-8'))


"""The given solution uses a tuple to compare multiple variables as one
for the match-case statements, which is objectively better:
"""

def greet(language_code):
    match language_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai!'

def extract_language(locale):
    return locale.split('_')[0]

def extract_region(locale):
    return locale.split('.')[0].split('_')[1]

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case _:
            return greet(language)
        
print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))
print(local_greet('ru_RU.UTF-8'))   # None


"""I still also like the user solution of using a dictionary (although
they forgot to manage what happens in the case of languages without a
specific greeting yet, as does the given solution):
"""

language_greetings = {
    'en' : {'US': 'Hey!', 'GB': 'Hello!', 'AU': 'Howdy!'},
    'fr' : 'Salut!',
    'pt' : 'Olá!',
    'de' : 'Hallo!',
    'sv' : 'Hej!',
    'af' : 'Haai!'
}

def greet(language, dialect = None):
    if language == 'en': 
        return language_greetings[language][dialect]
    else:
        return language_greetings[language]

def extract_language(locale):
    return locale[0:2]

def extract_dialect(locale):
    return locale[3:5]

def local_greet(locale):
    language = extract_language(locale)
    if language == 'en':
        dialect = extract_dialect(locale)
        return greet(language, dialect)

    return greet(language)

print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))
# print(local_greet('ru_RU.UTF-8'))     # KeyError