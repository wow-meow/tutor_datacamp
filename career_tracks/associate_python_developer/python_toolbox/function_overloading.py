#!/usr/bin/env python3
from typing import Union, overload


class Calculator:
    """Demonstrates different approaches to function overloading in Python"""

    # Method 1: Using default arguments
    def add_default(self, a: int, b: int = 0, c: int = 0):
        """Traditional Python way - using default arguments"""
        return a + 2 * b + 3 * c

    # Method 2: Using *args
    def add_args(self, *args):
        """Using variable arguments"""
        weights = range(1, len(args) + 1, 1)  # generate weightings
        res = 0
        for x, w in zip(args, weights):
            res += x * w
        return res

    # Method 3: Using type hints and Union
    def add_union(
        self, a: Union[int, float], b: Union[int, float]
    ) -> Union[int, float]:
        """Using Union type hints to accept multiple types"""
        return a + 2 * b

    # Method 4: Using @overload decorator (type checking only, needs implementation)
    @overload
    def add_overload(self, x: int, y: int) -> int: ...

    @overload
    def add_overload(self, x: float, y: float) -> float: ...

    def add_overload(self, x, y):
        """Actual implementation that handles both overloaded cases"""
        return x + 2 * y


if __name__ == "__main__":
    calc = Calculator()

    # Method 1: Default arguments
    print("\nUsing default arguments:")
    print("add_default(1):", calc.add_default(1))  # Uses defaults for b and c
    print("add_default(1, 2):", calc.add_default(1, 2))  # Uses default for c
    print("add_default(1, 2, 3):", calc.add_default(1, 2, 3))  # Uses all arguments

    # Method 2: Variable arguments
    print("\nUsing *args:")
    print(f"add_args(1): {calc.add_args(1)} == {1}")
    print(f"add_args(1, 2): {calc.add_args(1, 2)} == {1 + 2*2}")
    print(f"add_args(1, 2, 3, 4): {calc.add_args(1, 2, 3, 4)} == {1 + 2*2 + 3*3 + 4*4}")

    # Method 3: Union types
    print("\nUsing Union types:")
    print("add_union(1, 2):", calc.add_union(1, 2))  # integers
    print("add_union(1.5, 2.5):", calc.add_union(1.5, 2.5))  # floats

    # Method 4: @overload decorator
    print("\nUsing @overload decorator:")
    print("add_overload(1, 2):", calc.add_overload(1, 2))  # integers
    print("add_overload(1.5, 2.5):", calc.add_overload(1.5, 2.5))  # floats
