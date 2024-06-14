# Exercise 5 in the Loops exercises:

# Using the code below as a starting point, write a while loop that prints the 
# elements of lst at each index and terminates after printing the last element 
# of the list.

lst = []#[1, 3, 7, 15]
index = 0


while index < len(lst):
    print(lst[index])
    index += 1


# Further Exploration: What would the code output if lst is empty? Why is that?


# It would do nothing, since len(lst) is 0, so 0 is not < 0. However, if you 
# don't put the print statement inside the for loop, it would produce an 
# IndexError, since not even index 0 exists in lst.