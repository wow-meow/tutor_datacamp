#!/usr/bin/env python3

list_a = [1, 2, 3]
list_b = ["a", "b", "c"]
paired_generator = ((a, b) for a, b in zip(list_a, list_b))
print(list_a)
print(list_b)
print(list(paired_generator))


def generate_descending(n):
    for i in range(n, 0, -1):
        yield i


desc_numbers = generate_descending(5)
print(desc_numbers)
print(type(desc_numbers))
print(list(desc_numbers))
