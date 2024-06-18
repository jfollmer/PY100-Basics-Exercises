# Passcode exercise in Lists exercises:

"""We generated parts of a passcode and now want to combine them into a 
string. Write some code that returns a string, with each portion of the 
passcode separated by a hyphen (-).

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'
"""

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

print('-'.join(passcode))   # 11-jZ5-hQ3f*-8!7g3-p3Fs


# Given solution has a second solution using iteration, mentioning that
# it is less Pythonic:

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']
joined_passcode = ''

for i in range(len(passcode)):
    if i > 0:
        joined_passcode += '-'

    joined_passcode += passcode[i]

print(joined_passcode)  # 11-jZ5-hQ3f*-8!7g3-p3Fs