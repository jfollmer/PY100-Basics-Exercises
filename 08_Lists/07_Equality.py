# Equality exercise in Lists exercises:

# Predict the output of the code shown below. When you run the code, do 
# you see what you expected? Why or why not?

list1 = [2, 6, 4]
list2 = [2, 6, 4]

print(list1 == list2)


"""The expression passed to print() is testing for value equality, not
object equality, and the two lists are equal in value, so this should
print True, and it does.
"""