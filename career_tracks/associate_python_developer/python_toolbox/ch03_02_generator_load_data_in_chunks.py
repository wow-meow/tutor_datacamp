#!/usr/bin/env python3

from typing import TextIO

# Open a connection to the file
with open("world_dev_ind.csv") as file:
    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(1000):
        # Split the current line into a list: line
        line = file.readline().split(",")

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)


with open("world_dev_ind.csv") as file:
    data = file.readline()
    print()
    print(type(data))
    # Demonstrate newline character in the string
    print("Length with newline:", len(data))
    print("Raw string with newline:", repr(data))
    # Remove newline and show length
    data_strip = data.strip()
    print("Length without newline:", len(data_strip))
    print("Raw string without newline:", repr(data_strip))


# Define read_large_file()
def read_large_file(file_object: TextIO) -> str:
    """A generator function to read a large file lazily."""
    # Loop indefinitely until the end of the file
    while True:
        # Read a line from the file: data
        data = file_object.readline()
        # Break if this is the end of the file (readline() returns empty string at EOF)
        if not data:
            print("\nEOF is an empty str:", data)
            break
        # Yield the line of data
        yield data


# Open a connection to the file
with open("world_dev_ind.csv") as file:
    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

    for line in gen_file:
        print(line)

# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Open a connection to the file
with open("world_dev_ind.csv") as file:
    # Iterate over the generator from read_large_file()
    for line in read_large_file(file):
        row = line.split(",")
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

# Print
print(counts_dict)
