#!/usr/bin/env python3

import numpy as np
import pandas as pd

heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weights / heights ** 2
print(bmi)

print(f"2 > 3 : {2 > 3}")
print(f"2 >= 3 : {2 >= 3}")
print(f"2 >= 2 : {2 >= 2}")
print(f"'carl' < 'chris' : {'carl' < 'chris'}")

# Examples with apostrophes
# Using double quotes when string contains apostrophes
TEXT1 = "Don't worry about apostrophes when using double quotes"
TEXT2 = "It's easy to include apostrophes this way"

# If using single quotes, need to escape the apostrophe with backslash
TEXT3 = 'Don\'t forget to escape apostrophes with single quotes'

print('\n' + TEXT1)
print('\n' + TEXT2)
print('\n' + TEXT3)

# Multi-line strings examples
POEM1 = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''

# Triple double quotes work the same way
POEM2 = """First line
    Second line with indentation
        Third line with more indentation
Last line"""

# Multi-line string with mixed quotes
POEM3 = '''Here's a text that contains "quotes"
and can span across
multiple lines without any issues'''

print("\nUsing triple single quotes:")
print(POEM1)
print("\nUsing triple double quotes:")
print(POEM2)
print("\nMixed quotes in multi-line:")
print(POEM3)

print(bmi)
print(bmi > 23)

# Write code to see if True equals False.
print(True is False)
# Write Python code to check if -5 * 15 is not equal to 75.
print(-5 * 15 != 75)
# Ask Python whether the strings "pyscript" and "PyScript" are equal.
print("pyscript" == "PyScript")
# What happens if you compare booleans and integers?
# Write code to see if True and 1 are equal.
print(True == 1)

# Write Python expressions, wrapped in a print() function, to check whether:
# x is greater than or equal to -10. x has already been defined for you.
x = -3 * 6
print(x >= -10)
# "test" is less than or equal to y. y has already been defined for you.
y = "test"
print("test" <= y)
# True is greater than False.
print(True > False)

# Create arrays
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])
# Using comparison operators, generate boolean arrays that answer the following questions:
# You can also compare two NumPy arrays element-wise. Which areas in my_house are smaller 
# than the ones in your_house?
# Which areas in my_house are greater than or equal to 18?
# my_house greater than or equal to 18
print(my_house >= 18)
print(my_house[my_house >= 18])
# my_house less than your_house
print(my_house < your_house)
print(my_house[my_house < your_house])

# Find indexes and values that satisfy conditions
print("\nFinding entries and their indexes in NumPy arrays:")
# For my_house >= 18
# Get indexes where condition is True
indexes_ge_18 = np.where(my_house >= 18)[0]
values_ge_18 = my_house[indexes_ge_18]       # Get the actual values
print(f"Indices where my_house >= 18: {indexes_ge_18}")
print(f"Values where my_house >= 18: {values_ge_18}")

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0
# Write Python expressions, wrapped in a print() function, to check whether:
# my_kitchen is bigger than 10 and smaller than 18.
print(my_kitchen > 10 and my_kitchen < 18)
# my_kitchen is smaller than 14 or bigger than 17.
print(my_kitchen < 14 or my_kitchen > 17)
# double the area of my_kitchen is smaller than triple the area of your_kitchen.
print(2 * my_kitchen < 3 * your_kitchen)

# Generate boolean arrays that answer the following questions:
# Which areas in my_house are greater than 18.5 or smaller than 10?
print(np.logical_or(my_house > 18.5, my_house < 10))
print(np.where(np.logical_or(my_house > 18.5, my_house < 10))[0])
print(my_house[np.logical_or(my_house > 18.5, my_house < 10)])
# Which areas are smaller than 11 in both my_house and your_house?
print(np.logical_and(my_house < 11, your_house < 11))
print(np.where(np.logical_and(my_house < 11, your_house < 11))[0])