#!/usr/bin/env python3

from collections.abc import Iterable as IterableType
from typing import Any


class MyIterable:
    """
    A custom iterable class that yields integers from 1 to nitems.

    This class implements the iterator protocol, allowing it to be used
    in for loops and other iterable contexts. It generates a sequence of
    integers starting from 1 up to the specified number of items.

    Attributes:
        limit (int): The number of items to generate.
        counter (int): The current count in the iteration.

    Methods:
        __iter__: Returns the iterator object (self).
        __next__: Returns the next item in the sequence or raises StopIteration.
    """

    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __iter__(self):
        return self

    def _check_limit(self):
        """Check if iteration limit is reached"""

        # assert self.counter <= self.limit, (
        #     f"Counter ({self.counter}) exceeded limit ({self.limit}). "
        #     "This indicates a bug in the iterator implementation."
        # )

        if self.counter > self.limit:
            raise ValueError(f"Counter ({self.counter}) exceeded limit ({self.limit})")
        if self.counter == self.limit:
            raise StopIteration("Reached the limit!")

    def __next__(self):
        self._check_limit()
        self.counter += 1
        return self.counter


class String(MyIterable):
    """
    A custom string class that implements the iterable protocol.

    This class extends MyIterable to create an iterable string object.
    It allows iteration over individual characters of the string.

    Attributes:
        str_literal (str): The string to be iterated over.

    Methods:
        __init__: Initializes the String object with a given string.
        __next__: Returns the next character in the string or raises StopIteration.
    """

    def __init__(self, str_literal: str = ""):
        self.str_literal = str_literal
        super().__init__(len(str_literal))

    def __next__(self):
        self._check_limit()  # Reuse parent's limit checking
        char = self.str_literal[self.counter]
        self.counter += 10
        return char


def test_MyIterableClass(an_iterable: IterableType[Any]) -> None:
    typename = type(an_iterable).__name__

    if not isinstance(an_iterable, IterableType):
        raise TypeError(f"Expected an iterable, got {typename}")

    print(f"Testing {typename}:")
    it = iter(an_iterable)
    i = 0
    while True:
        try:
            print(next(it))
            i += 1
        except StopIteration as e:
            print(f"Iterator exhausted after {i} iterations.")
            print(f"StopIteration exception: {repr(e)}")
            print(f"Exception message: {str(e)}")
            return
        except ValueError as e:
            print(f"Error: {str(e)}")
            return  # Exit the function on error


# Test both iterables
test_MyIterableClass(MyIterable(3))
print()  # Empty line between tests
test_MyIterableClass(String("Hello, World!"))
