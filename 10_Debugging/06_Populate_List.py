# Populate List exercise in Debugging exercises:

"""You want to add the numbers from 1 to 5 to a list, but the code below 
is not producing the expected result. How can you fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)

"""


numbers = []

for i in range(6):      # changed 5 to 6 because stop is noninclusive
    numbers.append(i)

print(numbers)