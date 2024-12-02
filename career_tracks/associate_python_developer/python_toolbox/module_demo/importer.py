#!/usr/bin/env python3

print("1. Before importing main_check:")
print(f"2. My module name: {__name__}")

# Import our module
import main_check

print("\n3. After importing main_check:")
print(f"4. Using main_check's add function: {main_check.add(10, 5)}")
