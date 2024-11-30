#!/usr/bin/env python3

from typing import Union


def clean_string(
    text: str,
    *,
    remove_spaces: bool = True,
    space_to_underscore: bool = False,
    lower: bool = False,
) -> str:
    """Clean a string by replacing or removing spaces and optionally converting to lowercase.

    Args:
        text (str): The input string to clean.
        remove_spaces (bool, optional): If True, removes all spaces. Defaults to True.
        space_to_underscore (bool, optional): If True, replaces spaces with underscores. Defaults to False.
        lower (bool, optional): If True, converts the result to lowercase. Defaults to False.

    Returns:
        str: The cleaned string.

    Raises:
        TypeError: If input is not a string.
        ValueError: If input is an empty string or contains only whitespace.

    Note:
        If both remove_spaces and space_to_underscore are True, remove_spaces takes precedence.
    """
    # Type checking
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, got {type(text).__name__} instead")

    # Check for empty string
    if not text.strip():
        raise ValueError("Input string cannot be empty or only whitespace")

    # Clean the string
    if remove_spaces:
        ret = text.replace(" ", "")
    elif space_to_underscore:
        ret = text.replace(" ", "_")

    if lower:
        ret = ret.lower()

    return ret


# Test cases
test_strings = [
    "I LoVe dATaCamP!",  # Normal case
    "",  # Empty string
    "   ",  # Whitespace only
    123,  # Wrong type (int)
    None,  # None type
]

for s in test_strings:
    try:
        result = clean_string(s)
        print(f"Input: {s!r}")
        print(f"Output: {result!r}\n")
    except (TypeError, ValueError) as e:
        print(f"Error for input {s!r}: {str(e)}\n")


# Demonstrate method chaining
test_string = "I LoVe dATaCamP!"
print(f"Original:         {test_string}")
print("\nMethod chaining example:")
# Instance methods: easier to chain, more readable, Pythonic
result1 = test_string.replace(" ", "_").lower()
print(f"Instance methods: {result1}")
# String class methods: more verbose and harder to read
result2 = str.lower(str.replace(test_string, " ", "_"))
print(f"String methods:   {result2}")
# Both produce the same result
assert result1 == result2


password = "not_very_secure_2023"


# Define the password_checker function, which should accept one argument called submission.
def password_checker(submission: str = "") -> None:
    """_summary_

    Args:
        submission (str, optional): _description_. Defaults to "".
    """
    # Check that the password variable and the submission match
    if password == submission:
        print("Successful login!")
    # Otherwise, print "Incorrect password"
    else:
        print("Incorrect password")


# Call the function
password_checker("NOT_VERY_SECURE_2023")


# Define convert_data_structure with two arguments: data and data_type, where the latter has a default value of "list".
# Add a condition to check if data_type is "tuple".
# Else if data_type is "set", convert data into a set, saving it as a variable of the same name.
# Call the function on the data structure provided, using an appropriate keyword argument value-pair to convert it to a set.


# Create the convert_data_structure function
def convert_data_structure(
    data=Union[list, tuple, set], data_type: str = "list"
) -> Union[list, tuple, set]:
    """Convert a data structure to a list, tuple, or set.

    Args:
        data (list, tuple, or set): A data structure to be converted.
        data_type (str, optional): String representing the type of structure to convert data to. Defaults to "list".

    Returns:
        data (list, tuple, or set): Converted data structure.
    """

    # If data_type is "tuple"
    if data_type == "tuple":
        data = tuple(data)
    # Else if data_type is set, convert to a set
    elif data_type == "set":
        data = set(data)
    else:
        data = list(data)
    return data


# Call the function to convert to a set
convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type="set")

a_set = {"a", 1, "b", 2, "c", 3}
print(a_set)
print(type(a_set))


# Define a function called concat() that accepts arbitrary arguments called args.
def concat(*args) -> str:
    # Create an empty string
    result = ""
    # Iterate over the Python args tuple
    for arg in args:
        result += " " + arg
    return result


# Call the function
print(concat("Python", "is", "great!"))


# Define a function called concat
def concat2(**kwargs) -> str:
    # Create an empty string
    result = ""
    # Iterate over the Python kwargs
    for kwarg in kwargs.values():
        result += " " + kwarg
    return result


# Call the function
print(concat2(start="Python", middle="is", end="great!"))
