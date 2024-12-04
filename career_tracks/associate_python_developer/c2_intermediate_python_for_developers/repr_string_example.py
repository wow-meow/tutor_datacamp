#!/usr/bin/env python3

# Demonstrate the difference between !r and regular formatting
# Example values
text_with_quotes = 'Hello "World"'
text_with_newline = "Hello\nWorld"
special_chars = "\t\r\n"

print("\nDemonstrating !r formatting:")
print("1. Regular string vs !r with quotes:")
print(f"   Regular: {text_with_quotes}")  # Regular: Hello "World"
print(f"   With !r: {text_with_quotes!r}")  # With !r: 'Hello "World"'

print("\n2. Regular string vs !r with newline:")
print(f"   Regular: {text_with_newline}")  # Shows actual newline
print(f"   With !r: {text_with_newline!r}")  # Shows \n as text

print("\n3. Regular string vs !r with special characters:")
print(f"   Regular: {special_chars}")  # Shows actual whitespace
print(f"   With !r: {special_chars!r}")  # Shows \t\r\n as text
