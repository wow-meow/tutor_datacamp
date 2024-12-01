#!/usr/bin/env python3

from collections.abc import Iterable as IterableType
from typing import Any

from intro_to_iterators import MyIterable, String


def process_ints(iterable: IterableType[int]) -> None:
    """Only accepts iterables containing integers"""
    for i in iterable:
        print(i * 2)


def process_strs(iterable: IterableType[str]) -> None:
    """Only accepts iterables containing strings"""
    for s in iterable:
        print(s.upper())


def process_any(iterable: IterableType[Any]) -> None:
    """Accepts iterables containing any type"""
    for item in iterable:
        print(item)


# These would type check correctly with process_ints
process_ints([1, 2, 3])  # OK
process_ints(MyIterable(3))  # OK (returns ints)
process_ints(["a", "b"])  # Type error! (strings, not ints)

# These would type check correctly with process_strs
process_strs(["a", "b"])  # OK
process_strs(String("Hi"))  # OK (returns strings)
process_strs([1, 2, 3])  # Type error! (ints, not strings)

# These would all type check correctly with process_any
process_any([1, 2, 3])  # OK
process_any(["a", "b"])  # OK
process_any(MyIterable(3))  # OK
process_any(String("Hi"))  # OK
