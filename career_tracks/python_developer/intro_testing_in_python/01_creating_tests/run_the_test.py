#!/usr/bin/env python3
"""
Module for demonstrating testing in Python.
Contains mathematical operations and their corresponding tests.
"""


# Standard library imports
import logging
from typing import Union
import os

# Third-party imports (if any)
import pytest

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
FILE_PATH = os.path.join(os.path.dirname(__file__), 'hello_world.txt')
ENCODING = "utf-8"

# Custom exceptions (if needed)
class MathOperationError(Exception):
    """Custom exception for math operation errors."""
    pass

# Helper functions
def write_to_file(content: str, filepath: str = FILE_PATH) -> None:
    """
    Helper function to write content to a file.

    Raises:
        IOError: If there is an error writing to the file, with details about the specific error.
    """
    try:
        with open(filepath, 'w', encoding=ENCODING) as f:
            f.write(content + "\n")
    except IOError as e:
        logger.error(f"Failed to write to file: {e}")
        raise

def is_even(number: Union[int, float]):
    """
    Check if a number is even.

    Args:
        number (int or float): The number to check. Must be a whole number and non-zero.

    Returns:
        bool: True if the number is even, False if odd.

    Raises:
        TypeError: If the input is not a number.
        ValueError: If the input is not a whole number or is zero.
        RuntimeError: If an unexpected error occurs during the check.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(3)
        False
        >>> is_even(-2)
        True
        >>> is_even(0)
        Raises ValueError: Input cannot be zero
        >>> is_even(3.14)
        Raises ValueError: Input must be a whole number
        >>> is_even("2")
        Raises TypeError: Input must be a number
    """
    try:
        if not isinstance(number, (int, float)):
            raise TypeError("Input must be a number")
        if isinstance(number, float) and not number.is_integer():
            raise ValueError("Input must be a whole number")
        if number == 0:
            raise ValueError("Input cannot be zero")
        return int(number) % 2 == 0
    except Exception as e:
        if isinstance(e, (TypeError, ValueError)):
            raise # This re-raises TypeError or ValueError with original traceback
        raise RuntimeError(f"Unexpected error: {e}")

def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Divides two numbers and returns the result.

    Args:
        a (int or float): The dividend (numerator)
        b (int or float): The divisor (denominator)

    Returns:
        int or float: The result of dividing a by b. For integer inputs, returns
                     integer division result. For floating point inputs, returns
                     float result rounded to 10 decimal places.

    Raises:
        ValueError: If either input is not a number (int or float)
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(10, 2)
        5
        >>> divide(10.0, 3)
        3.3333333333
        >>> divide(1, 0)
        Raises ZeroDivisionError: Cannot divide by zero!
        >>> divide("10", 2)
        Raises ValueError: Inputs must be numbers
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Inputs must be numbers")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        if isinstance(a, float) or isinstance(b, float):
            # Handle floating point division
            result = round(a / b, 10)  # Round to 10 decimal places for precision
            return result
        return a / b
    except TypeError:
        raise ValueError("Inputs must be numbers")

"""Test suite for is_even() function.

Verifies:
-[ ] Even/odd number detection
-[ ] Negative number handling 
-[ ] Zero validation 
-[ ] Type checking
-[ ] Float validation
-[ ] Large integer edge cases
"""

def test_is_even_valid_numbers() -> None:
    # Test valid even number
    assert is_even(4) == True
    # Test valid odd number
    assert is_even(3) == False

def test_is_even_negative_numbers() -> None:
    # Test negative even number
    assert is_even(-4) == True
    # Test negative odd number
    assert is_even(-3) == False

def test_is_even_zero() -> None:
    # Test zero input
    with pytest.raises(ValueError, match="Input cannot be zero"):
        is_even(0)

def test_is_even_non_numeric() -> None:
    # Test non-numeric input
    with pytest.raises(ValueError, match="Input must be a number"):
        is_even("not a number")

def test_is_even_float() -> None:
    # Test floating point number
    with pytest.raises(ValueError, match="Input must be a whole number"):
        is_even(3.14)

def test_is_even_large_number() -> None:
    # Test very large number
    assert is_even(1000000000) == True
    assert is_even(999999999) == False

"""Test functions for divide()

Tests division operations including:
-[x] Division of valid numbers
-[x] Division by zero handling
-[x] Negative number handling
-[x] Floating point division
-[x] Type validation
-[x] Edge cases with very large/small numbers
"""

def test_divide_valid_numbers():
    # Test basic integer division
    assert divide(10, 2) == 5
    # Test division resulting in whole number
    assert divide(100, 4) == 25
    # Test division with decimal result
    assert divide(10, 3) == 3.3333333333
    # Test division of equal numbers
    assert divide(7, 7) == 1

def test_divide_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero!"):
        divide(10, 0)

def test_divide_negative():
    # Test negative divisor
    assert divide(10, -2) == -5
    # Test negative dividend 
    assert divide(-10, 2) == -5
    # Test both negative numbers
    assert divide(-10, -2) == 5

def test_divide_float():
    # Test float division with integer result
    assert divide(33, 3.3) == 10
    # Test float division with decimal result 
    assert divide(10.0, 3) == 3.3333333333
    # Test both float inputs
    assert divide(5.5, 2.2) == 2.5

def test_divide_type_errors():
    # Test string input
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        divide("10", 2)
    # Test list input
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        divide([1,2,3], 2)
    # Test None input
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        divide(None, 5)
    # Test invalid second parameter
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        divide(10, "2")

def test_divide_edge_cases():
    # Test very large numbers
    assert divide(1e15, 1e5) == 1e10
    # Test very small numbers 
    assert divide(1e-10, 1e5) == 1e-15
    # Test large divided by small
    assert divide(1e15, 1e-15) == 1e30
    # Test small divided by large
    assert divide(1e-15, 1e15) == 1e-30
    # Test numbers near system float limits
    assert divide(1.7976931348623157e+308, 1e+100) == 1.7976931348623157e+208  # Near max float
    assert divide(2.2250738585072014e-308, 1e+100) == 2.2250738585072014e-408  # Near min float

# Main execution
if __name__ == "__main__":
    # Code that should only run when the module is executed directly
    try:
        # Test file writing with different content
        write_to_file("Hello, World!")
        write_to_file("Testing 123")
        write_to_file("Special chars: !@#$%")
        write_to_file("Multiple\nLines\nTest")
        # Test even/odd numbers
        print(f"Is 4 an even number? {is_even(4)}")
        print(f"Is 7 even? {is_even(7)}")
        print(f"Is 100 even? {is_even(100)}")
        print(f"Is -6 even? {is_even(-6)}")
        print(f"Is 0 even? {is_even(0)}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        
    # Run all tests
    pytest.main([__file__])