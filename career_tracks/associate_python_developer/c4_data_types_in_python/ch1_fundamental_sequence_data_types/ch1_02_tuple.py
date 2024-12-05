#!/usr/bin/env python3

"""Demonstrates tuple features and usage in Python.

This module shows various tuple operations and characteristics including:
- Creating tuples using parentheses and trailing commas
- Accessing tuple methods like index() and count()
- Using zip() to combine lists into tuples
- Tuple unpacking with multiple assignment
- Identifying accidental tuple creation from trailing commas

Key characteristics of Tuple:
- Immutable - contents cannot be modified after creation
- Memory efficient compared to lists
- Maintains insertion order of elements
- Supports indexing and slicing
- Allows unpacking into multiple variables

The examples use real-world data (popular baby names) to demonstrate practical tuple usage.
"""

a_tup = ('b', 'a', 'a', 'c', 'a')
print(a_tup)
print(a_tup.index('a'))
print(a_tup.count('a'))
print(a_tup[1:4])
print(a_tup[1:4].index('a'))
print(a_tup[1:4].count('a'))

girl_names = [
    'Jada', 'Emily', 'Ava', 'Serenity', 'Claire',
    'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail', 
    'Zoe', 'Leah', 'Hailey', 'Ava', 'Olivia', 
    'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela',
    'Camila', 'Savannah', 'Serenity', 'Chloe', 'Fatoumata'
    ]

boy_names = [
    'Josiah', 'Ethan', 'David', 'Jayden', 'Mason',
    'Ryan', 'Christian', 'Isaiah', 'Jayden', 'Michael',
    'Noah', 'Samuel', 'Sebastian', 'Noah', 'Dylan',
    'Lucas', 'Joshua', 'Angel', 'Jacob', 'Matthew',
    'Josiah', 'Jacob', 'Muhammad', 'Alexander', 'Jason'
    ]


# Use the zip() function to pair up girl_names and boy_names into a variable called pairs.
pairs = zip(girl_names, boy_names)

# Use a for loop to loop through pairs, using enumerate() to keep track of your position.
# Unpack pairs into the variables rank and pair.
for rank, pair in enumerate(pairs):
    # Unpack pair: girl_name, boy_name
    girl_name, boy_name = pair
    # Print the rank, girl name, and boy name, in that order. The rank is contained in rank.
    print(f'Rank {rank+1}: {girl_name} and {boy_name}')


# Create a variable named normal and set it equal to 'simple'.
normal = 'simple'
# Create the mistaken variable: error
# Create a variable named error and set it equal to 'trailing comma',.
error = 'trailing comma',
# Print the type of the normal and error variables.
print(type(normal))
print(type(error))
