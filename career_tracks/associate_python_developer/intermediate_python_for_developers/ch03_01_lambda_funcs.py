#!/usr/bin/env python3

from typing import Union, Sequence

# For sequences (lists, tuples)
average_lam = lambda x: sum(x) / len(x)

# For both individual numbers and sequences
average_lam2 = lambda *args: sum(
    args[0] if len(args) == 1 and isinstance(args[0], (list, tuple)) else args
) / (
    len(args[0]) if len(args) == 1 and isinstance(args[0], (list, tuple)) else len(args)
)


def average(*args: Union[int, float]) -> float:
    """Calculate the average of any number of numeric arguments.

    Args:
        *args (a tuple of Union[int, float]): Variable number of integers or floating
        point numbers

    Returns:
        res (float): The arithmetic mean of all arguments

    Raises:
        ZeroDivisionError: If no arguments are provided
    """
    res = sum(args) / len(args)
    return res


def flexible_average(*args: Union[int, float, Sequence[Union[int, float]]]) -> float:
    """Calculate average of numbers, accepting either a sequence or individual numbers.

    Args:
        *args: Either a single sequence of numbers or individual numbers

    Returns:
        float: The arithmetic mean

    Examples:
        >>> flexible_average([1, 2, 3])  # List input
        2.0
        >>> flexible_average(1, 2, 3)    # Individual numbers
        2.0
    """
    if len(args) == 1 and isinstance(args[0], (list, tuple)):
        print(args)
        print(args[0])
        numbers = args[0]
    else:
        print(args)
        numbers = args
    return sum(numbers) / len(numbers)


# Test cases
numbers = [1, 3, 5, 7, 9]
print("\nTesting average_lam2:")
print(f"With list: {average_lam2(numbers)}")  # Passing a list
print(
    f"With individual numbers: {average_lam2(1, 3, 5, 7, 9)}"
)  # Passing individual numbers
print(f"With regular function (list): {flexible_average(numbers)}")
print(f"With regular function (individual): {flexible_average(1, 3, 5, 7, 9)}")

names = ["john", "sally", "leah"]
names_capitalized = map(lambda x: x.capitalize(), names)
print(f"\nCapitalized names: {list(names_capitalized)}")

sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]
# Create add_taxes to add 20% to each item in sales_prices
add_taxes = list(map(lambda x: round(1.2 * x, 2), sales_prices))
add_taxes2 = [round(1.2 * x, 2) for x in sales_prices]
# Use add_taxes to return a new list with updated values
print(f"\nPrices with 20% tax: {add_taxes}")
print(f"\nPrices with 20% tax: {add_taxes2}")
assert add_taxes == add_taxes2

# Calculate each number raised to itself (e.g., 1¹, 3³, 5⁵, etc.)
power_lam = lambda x, y: x**y
# Unzip numbers to use as both base and exponent
# powers = list(map(power_lam, numbers, numbers))
# powers = [power_lam(x, x) for x in numbers]
# powers = [(lambda x, y: x**y)(x, x) for x in numbers]
powers = [x**x for x in numbers]
print(f"\nNumbers raised to themselves: {powers}")
