# Exercise 3 in the Loops exercises:

# Write a loop that prints the value of the greeting variable three times.

greeting = 'Aloha!'


for i in range(3):
    print(greeting)


# Solution also gives a while loop version, but mentions that a range is still
# the most Pythonic way to do this:

count = 1
while count <= 3:
    print(greeting)
    count += 1

# It also mentions a convention to use _ when you don't need an actual loop
# variable:

for _ in range(3):
    print(greeting)