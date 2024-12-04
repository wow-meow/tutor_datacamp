#!/usr/bin/env python3

"""Demonstrate creating DataFrames from lists of dictionaries.

This script shows:
- Basic DataFrame creation from list of dicts
- Handling missing values
- Specifying column order
- Adding/modifying columns
- Different ways to view the data
"""

import pandas as pd
from pprint import pprint

# Sample data: list of dictionaries
users = [
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Anna", "age": 22, "city": "Paris"},
    {"name": "Peter", "age": 35, "city": "London"},
    {"name": "Linda", "age": 25, "city": "Berlin"},
]

print("\nOriginal data (list of dicts):")
pprint(users)

# Create DataFrame from list of dicts
df = pd.DataFrame(users)
print("\nBasic DataFrame:")
print(df)

# With missing data
users_missing = [
    {"name": "John", "age": 28, "city": "New York"},
    {"name": "Anna", "city": "Paris"},  # Missing age
    {"name": "Peter", "age": 35},  # Missing city
]

df_missing = pd.DataFrame(users_missing)
print("\nDataFrame with missing values:")
print(df_missing)

# Specify column order
columns = ["name", "city", "age"]
df_ordered = pd.DataFrame(users, columns=columns)
print("\nDataFrame with specified column order:")
print(df_ordered)

# Add new column using list comprehension
df["country"] = [
    city + ", USA" if city == "New York" else city + ", EU" for city in df["city"]
]
print("\nDataFrame with new column:")
print(df)

# Display info about DataFrame
print("\nDataFrame info:")
df.info()

# Display basic statistics
print("\nDataFrame description:")
print(df.describe())

# Access specific columns
print("\nNames and ages:")
print(df[["name", "age"]])
