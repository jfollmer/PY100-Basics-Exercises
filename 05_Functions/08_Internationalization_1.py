# Internationalization 1 exercise in the Functions exercises:

"""Use Python's control structures to create a function that takes an 
ISO 639-1 language code 
(https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes)
and returns a greeting in that language. You can take the examples below 
or add whatever languages you like.

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

"""


supported_language_codes = [
    'en', 'fr', 'pt', 
    'de', 'sv', 'af', 
    'it', 'es', 'ja', 
    'zh', 'uk'
    ]

def greet(language_code):
    match language_code:
        case 'en':              # English
            print('Hi!')
        case 'fr':              # Français (French)
            print('Salut!')
        case 'pt':              # Português (Portuguese)
            print('Olá!')
        case 'de':              # Deutch (German)
            print('Hallo!')
        case 'sv':              # Svenska (Swedish)
            print('Hej!')
        case 'af':              # Afrikaans
            print('Haai!')
        case 'it':              # Italiano (Italian)
            print('Salve!')
        case 'es':              # Español (Spanish)
            print('Hola!')
        case 'ja':              # 日本語 (Japanese)
            print('こんにちは!')
        case 'zh':              # 中文 (Chinese (Mandarin))
            print('你好!')
        case 'uk':              # Українська Мова (Ukrainian)
            print('Привіт!')
        case _:
            print('This language is not currently supported.')

for code in supported_language_codes:
    greet(code)


# I like this student solution's approach (I don't think CONV_MAP needs 
# to be a constant though, since you might add languages later):

CONV_MAP = {
    'en': 'Hi!',
    'fr': 'Salut!',
    'pt': 'Olá!',
    'de': 'Hallo!',
    'sv': 'Hej!',
    'af': 'Haai!',
}

def greet(code):
    if code in CONV_MAP:
        return CONV_MAP[code]
    else:
        return 'Invalid code'

print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!
print(greet('ja'))         # Invalid code!