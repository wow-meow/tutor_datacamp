#!/usr/bin/env python3

"""
A script demonstrating various Python ecosystem features.

This script showcases the usage of different Python modules and functions,
including os for file system operations, string for ASCII character sets,
and datetime for date manipulation. It also demonstrates basic Python
syntax and printing techniques.
"""

import os
import string
from datetime import date
import pandas as pd
# import numpy as np

pwd_str = os.getcwd()
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
os.chdir("./intermediate_python_for_developers")
print(os.getcwd())

# attribute, not a function
# print(os.environ)
# Print all ASCII lowercase characters
print(string.ascii_lowercase)
# Print all punctuation
print(string.punctuation)

# Create a variable called deadline, assigning a call of date(),
# passing in the numbers 2024, 1, and 19, in that order, separated by commas.
deadline = date(2024, 1, 19)
# Check the data type of deadline.
print(type(deadline))
# Print the deadline variable.
print(deadline)

# define each column of the dataframe using dict { column_label: column value list }
sales = {
    "user_id": ["KM37", "PR19", "YU88", "JB18", "LP65", "HJ11", "PR19", "IJ54"],
    "date": [
        "01/05/2024",
        "01/05/2024",
        "01/06/2024",
        "01/06/2024",
        "01/06/2024",
        "01/06/2024",
        "01/07/2024",
        "01/07/2024",
    ],
    "order_value": [197.75, 208.21, 134.99, 317.81, 201.3, 157.87, 99.99, 124.5],
}

# Import the pandas module using an alias of pd.
# import pandas as pd
# Create sales_df by using a pandas function to convert sales into a DataFrame.
sales_df = pd.DataFrame(sales)
# Preview the first five rows of sales_df.
print(sales_df.head(5))

print("\nComparing different ways to get first 5 rows:")
print("Are head(5) and [:5] equal?")
print(sales_df.head(5).equals(sales_df[:5]))

# Compare values element by element
print("\nElement-wise comparison:")
print((sales_df.head(5) == sales_df[:5]).all().all())
# Another way using iloc
print("\nComparing with iloc:")
print(sales_df.iloc[:5].equals(sales_df[:5]))

# Save the DataFrame to a CSV file
# index=False prevents writing row numbers as a separate column
sales_df.to_csv("sales.csv", index=False)
print("\nDataFrame has been saved to 'sales.csv'")
sales_df2 = pd.read_csv("sales.csv")

# pd.DataFrame.rename()
sales_df2.rename(
    index={0: "Hi0", 2: "Hi2", 7: "Hi7"}, columns={"date": "Hi-date"}, inplace=True
)
print(sales_df2)
