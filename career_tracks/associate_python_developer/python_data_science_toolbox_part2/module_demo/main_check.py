#!/usr/bin/env python3

print(f"1. Module name when run directly: {__name__}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Code inside this block only runs if this file is run directly
if __name__ == "__main__":
    print("2. This code runs only when the file is run directly")
    print("3. Testing add function:", add(5, 3))
else:
    print("4. This code runs when the file is imported as a module")
