#!/usr/bin/env python3

"""Demonstrates various applications of list comprehensions in Python.

This module showcases different ways to use list comprehensions, including:
- Basic list comprehensions with single expressions
- Matrix creation using nested list comprehensions
- Conditional list comprehensions (filtering with if)
- Conditional expressions in list comprehensions (if/else)
- Dictionary comprehensions
- Practical examples with strings and numbers

Examples include:
- Creating lists of characters from strings
- Generating squares of numbers
- Building matrices
- Filtering strings by length
- Converting lists to dictionaries with computed values
"""

doctor = ['house', 'cuddy', 'chase', 'thirteen', 'wilson']
a_list = [ doc[0] for doc in doctor ]
print(a_list)

# Create list comprehension: squares
squares = [i ** 2 for i in range(10)]

# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(5)] for row in range(5)]
# Print the matrix
for row in matrix:
    print(row)

nums = [num ** 2 for num in range(10) if num % 2 == 0]
print(nums)
nums2 = [num ** 2 if num % 2 == 0 else 0 for num in range(10)]
print(nums2)

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use member as the iterator variable in the list comprehension. 
# For the conditional, use len() to evaluate the iterator variable. 
# Note that if the number of characters is >= 7, 
# else replace it with an empty string - that is, '' or "".
new_fellowship = [ member for member in fellowship if len(member) >= 7 ]
new_fellowship2 = [ member for member in fellowship if len(member) >= 7 ]
new_fellowship3 = [ member if len(member) >= 7 else "" for member in fellowship ]
# Method 1: Using filter() with lambda
new_fellowship4 = list(filter(lambda x: len(x) >= 7, fellowship))

# Create a dict comprehension where the key is a string in fellowship 
# and the value is the length of the string. Remember to use the syntax <key> : <value> 
# in the output expression part of the comprehension to create the members of the dictionary. Use member as the iterator variable.
new_fellowship5 = { member: len(member) for member in fellowship }

print(new_fellowship)
print(new_fellowship2)
print(new_fellowship3)
print("Filter with lambda:", new_fellowship4)
print("dict comprehension:", new_fellowship5)
