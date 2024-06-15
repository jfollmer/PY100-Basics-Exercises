# Display Division exercise in the Functions exercises:

# Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three


"""Without the parentheses on line 12, this never prints. But it would
print the following if they were there:
3 / 1 = 3
6 / 2 = 3
9 / 3 = 3
12 / 4 = 3
...
30 / 10 = 3
"""