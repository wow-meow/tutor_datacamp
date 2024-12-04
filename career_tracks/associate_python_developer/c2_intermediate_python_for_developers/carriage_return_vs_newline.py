#!/usr/bin/env python3

import time
import sys


# \n (newline) - moves cursor to the start of next line
print("Demonstrating \\n (newline):")
text_with_n = "First line\nSecond line"
print(f"With \\n: {text_with_n!r}")
print("Result:")
print(text_with_n)

print("\n" + "=" * 50 + "\n")

# \r (carriage return) - moves cursor to start of current line
print("Demonstrating \\r (carriage return):")
text_with_r = "Hello\rWorld"
print(f"With \\r: {text_with_r!r}")
print("Result (notice how 'World' overwrites 'Hello'):")
print(text_with_r)

print("\n" + "=" * 50 + "\n")


# Practical example of \r - Progress bar
def show_progress():
    """_summary_"""
    for i in range(100 + 1):
        # \r moves cursor to start, next print overwrites previous
        sys.stdout.write(f"\rProgress: {i}%")
        sys.stdout.flush()  # Force output to display immediately
        time.sleep(0.05)
    print()  # Move to next line when done


print("Demonstrating \\r in a progress bar:")
show_progress()
