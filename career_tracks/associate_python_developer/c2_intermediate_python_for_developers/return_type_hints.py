#!/usr/bin/env python3
from typing import List, Union, Optional


# 1. Basic return type hint
def greet(name: str) -> str:
    """Return type hint indicates this function returns a string"""
    return name.upper()  # This is fine
    # return 42  # Type checker would warn about this


# 2. Multiple possible return types
def process_number(num: float) -> Union[float, str]:
    """Can return either float or string

    Args:
        num (float): _description_

    Returns:
        Union[float, str]: _description_
    """

    if num < 0:
        return "Negative numbers not allowed"
    return num * 2.0


# 3. Optional return (can return None)
def find_index(items: List[str], target: str) -> Optional[int]:
    """Return type can be int or None"""
    try:
        return items.index(target)
    except ValueError:
        return None


# 4. Return type doesn't affect runtime behavior
def add_numbers(a: int, b: int) -> str:  # Incorrectly hints str return
    """Type hint says returns str, but actually returns int
    Type checker would warn, but code still runs"""
    return a + b  # Returns int, despite hint saying str


# Example usage
print("1. Basic return type hint:")
result1 = greet("python")  # Type hint helps IDE suggest string methods
print(f"result1: {result1} (type: {type(result1).__name__})")

print("\n2. Union return type:")
result2a = process_number(5.0)  # Returns float
result2b = process_number(-5.0)  # Returns str
print(f"result2a: {result2a} (type: {type(result2a).__name__})")
print(f"result2b: {result2b} (type: {type(result2b).__name__})")

print("\n3. Optional return type:")
result3a = find_index(["a", "b", "c"], "b")  # Returns int
result3b = find_index(["a", "b", "c"], "z")  # Returns None
print(f"result3a: {result3a} (type: {type(result3a).__name__})")
print(f"result3b: {result3b} (type: {type(result3b).__name__})")

print("\n4. Mismatched return type:")
result4 = add_numbers(1, 2)  # Returns int despite str hint
print(f"result4: {result4} (type: {type(result4).__name__})")

# Type hints can be checked with tools like mypy
print("\nNote: Run 'mypy return_type_hints.py' to check type hints")
