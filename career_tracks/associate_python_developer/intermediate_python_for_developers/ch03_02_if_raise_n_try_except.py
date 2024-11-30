#!/usr/bin/env python3

from typing import Union

# Use a keyword allowing you to attempt to run code that cleans text.
# Swap a space for a single underscore in the text argument.
# Use another keyword that prints a helpful message if an error occurs
# when calling the snake_case() function.


def snake_case(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"Input must be a string, got {type(text).__name__} instead")

    if not text.strip():
        raise ValueError("Input string cannot be empty or only whitespace")

    # Swap spaces for underscores
    clean_text = text.replace(" ", "_")
    clean_text = clean_text.lower()
    return clean_text


test_strings = ["User Name 187", "", "    ", 168, None]

for s in test_strings:
    try:
        ret = snake_case(s)
        print(f"Input: {s!r}")
        print(f"Output: {ret!r}\n")
    except (TypeError, ValueError) as e:
        print(f"Error for input {s!r}: {str(e)}\n")
