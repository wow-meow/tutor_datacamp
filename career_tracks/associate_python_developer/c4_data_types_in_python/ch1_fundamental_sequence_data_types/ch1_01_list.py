#!/usr/bin/env python3

"""Demonstrates list features and usage in Python.

This module shows various list operations and characteristics including:
- Creating lists using square brackets
- List methods like extend(), index(), and pop()
- List comprehensions for data transformation
- Working with nested lists (records)

Key characteristics of List:
- Mutable - contents can be modified after creation
- Maintains insertion order of elements
- Supports indexing and slicing
- Can contain mixed data types
- Dynamic sizing - grows and shrinks as needed

The examples use real-world data (popular baby names) to demonstrate practical list usage.
"""

# Create a list called baby_names with the names 'Ximena', 'Aliza', 'Ayden', and 'Calvin'.
baby_names = ["Ximena", "Aliza", "Ayden", "Calvin"]

# Use the .extend() method on baby_names to add 'Rowen' and 'Sandeep' and print the list.
baby_names.extend(["Rowen", "Sandeep"])
print(baby_names)

# Use the .index() method to find the position of 'Rowen' in the list. Save the result as position.
position = baby_names.index("Rowen")

# Use the .pop() method with position to remove 'Rowen' from the list.
baby_names.pop(position)

# Print baby_names
print(baby_names)


records = [
    ["2014", "F", "20799", "Emma"],
    ["2014", "F", "19674", "Olivia"],
    ["2014", "F", "18490", "Sophia"],
    ["2014", "F", "16950", "Isabella"],
    ["2014", "F", "15586", "Ava"],
    ["2014", "F", "13442", "Mia"],
    ["2014", "F", "12562", "Emily"],
    ["2014", "F", "11985", "Abigail"],
    ["2014", "F", "10247", "Madison"],
    ["2014", "F", "10048", "Charlotte"],
    ["2014", "F", "9564", "Harper"],
    ["2014", "F", "9542", "Sofia"],
    ["2014", "F", "9517", "Avery"],
    ["2014", "F", "9492", "Elizabeth"],
    ["2014", "F", "8727", "Amelia"],
    ["2014", "F", "8692", "Evelyn"],
    ["2014", "F", "8489", "Ella"],
    ["2014", "F", "8469", "Chloe"],
    ["2014", "F", "7955", "Victoria"],
    ["2014", "F", "7589", "Aubrey"],
    ["2014", "F", "7554", "Grace"],
    ["2014", "F", "7358", "Zoey"],
    ["2014", "F", "7061", "Natalie"],
    ["2014", "F", "6950", "Addison"],
    ["2014", "F", "6869", "Lillian"],
    ["2014", "F", "6767", "Brooklyn"],
]

# Create the list comprehension: baby_names
baby_names = [row[-1] for row in records]

# Print the sorted baby names in ascending alphabetical order
print(sorted(baby_names, reverse=False))
