# In the Reading Documentation 1 exercises:

# Python lists come with a variety of built-in methods that allow for common list manipulations. One such operation is determining the index of an item in the list.

# Given a list:
fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
# How would you determine the index of the fruit "cherry" in this list?

# Standard Library -> Built-in Types -> Sequence Types - list, tuple, range >
#                                                   Common Sequence Operations

# seq.index(x [, i] [, j]])

# Index of the first occurrence of x in seq in index_range(i:j)

# ValueError if not found. Good practice to first check whether the value
# exists in the list using the in keyword before attempting to find its index.

print("cherry" in fruits)
print(fruits.index("cherry"))   # 2