#!/usr/bin/env python3

"""Demonstrates dictionary features and usage in Python.

This module showcases various dictionary operations and characteristics using
real-world data (art galleries and squirrels) as examples.

Key Characteristics:
    - Mutable: Contents can be modified after creation
    - Unordered: Does not maintain insertion order of elements
    - No Slicing: Cannot be accessed using slice notation
    - Unique Keys: Keys must be unique and immutable
    - Efficient: O(1) lookup by key
    - Dynamic: Supports runtime addition and removal of key-value pairs

Features Demonstrated:
    - Type Hints: Proper type annotation for dictionaries
    - Dictionary Creation:
        * Empty dictionary initialization
        * Creating from list of tuples
    - Safe Access:
        * dict.get() method for safe value retrieval
        * Built-in exception handling via get()
    - Sorting:
        * sorted(dict) operates on keys only by default
        * Custom sorting using key function:
            - Sort by values using lambda
            - Sort by key length
            - Sort by specific value attributes
            - Reverse sorting

Methods Covered:
    - get(): Safe value retrieval with optional default
    - items(): Access key-value pairs
    - sorted(): Key-based dictionary sorting with custom options
"""

art_galleries: dict[str, str] = {}

galleries: list[tuple[str, str]] = [
    ("MOMA", "10019"),  # 53rd Street
    ("Guggenheim", "10128"),  # Upper East Side
    ("Met", "10028"),  # Fifth Avenue
    ("Whitney", "10014"),  # Meatpacking District
    ("New Museum", "10002"),  # Bowery
    ("ICP", "10036"),  # Midtown
    ("Pace Gallery", "10001"),  # Chelsea
    ("David Zwirner", "10001"),  # West 20th Street
    ("Gagosian", "10075"),  # Upper East Side
    ("The Frick", "10065"),  # East 70th Street
    ("Hauser & Wirth", "10011"),  # West 22nd Street
    ("Marlborough", "10012"),  # Greenwich Village
    ("Lehmann Maupin", "10003"),  # University Place
    ("Galerie Lelong", "10001"),  # West 26th Street
    ("Paula Cooper", "10011"),  # West 21st Street
]

for name, zipcode in galleries:
    art_galleries[name] = zipcode

print()
for x in list(art_galleries.items())[-5:]:
    print(x)

print()
for name in sorted(art_galleries)[-5:]:
    print(f"{name}: {art_galleries[name]}")

print()
# This will sort by (key, value) tuples
for name, zipcode in sorted(art_galleries.items())[-5:]:
    print(name, zipcode)

print(art_galleries.get("Louvre"))
print(art_galleries.get("Louvre", "Not Found"))
print(art_galleries.get("Paula Cooper"))


squirrels = [
    ("Marcus Garvey Park", ("Black", "Cinnamon", "Cleaning", None)),
    (
        "Highbridge Park",
        ("Gray", "Cinnamon", "Running, Eating", "Runs From, watches us in short tree"),
    ),
    ("Madison Square Park", ("Gray", None, "Foraging", "Indifferent")),
    ("City Hall Park", ("Gray", "Cinnamon", "Eating", "Approaches")),
    ("J. Hood Wright Park", ("Gray", "White", "Running", "Indifferent")),
    ("Seward Park", ("Gray", "Cinnamon", "Eating", "Indifferent")),
    ("Union Square Park", ("Gray", "Black", "Climbing", None)),
    ("Tompkins Square Park", ("Gray", "Gray", "Lounging", "Approaches")),
]

# Create an empty dictionary: squirrels_by_park
squirrels_by_park: dict[str, tuple] = {}

# Loop over the squirrels list and unpack each tuple
for park, squirrel_details in squirrels:
    # Add each squirrel_details to the squirrels_by_park dictionary using the park as the key
    squirrels_by_park[park] = squirrel_details

# Sort the squirrels_by_park dict alphabetically by park
for park in sorted(squirrels_by_park):
    # Print each park and its value in squirrels_by_park
    print(f"{park}: {squirrels_by_park[park]}")

# Safely print 'Union Square Park' from the squirrels_by_park dictionary
print(squirrels_by_park.get("Union Square Park"))

# Safely print the type of 'Fort Tryon Park' from the squirrels_by_park dictionary
print(type(squirrels_by_park.get("Fort Tryon Park")))

# Safely print 'Central Park' from the squirrels_by_park dictionary or 'Not Found'
print(squirrels_by_park.get("Central Park", "Not Found"))

# Different ways to sort dictionaries
print("\nDifferent sorting examples:")
# 1. Sort by keys (default)
print("Sorted by keys:")
for park in sorted(squirrels_by_park):
    print(f"{park}: {squirrels_by_park[park]}")

# 2. Sort by primary fur color (first element of the value tuple)
print("\nSorted by primary fur color:")
for park in sorted(squirrels_by_park, key=lambda x: squirrels_by_park[x][0]):
    print(f"{park}: {squirrels_by_park[park]}")

# 3. Sort by activity (third element of the value tuple)
print("\nSorted by activity:")
for park in sorted(squirrels_by_park, key=lambda x: squirrels_by_park[x][2]):
    print(f"{park}: {squirrels_by_park[park]}")

# 4. Sort by park name length
print("\nSorted by park name length:")
for park in sorted(squirrels_by_park, key=len):
    print(f"{park}: {squirrels_by_park[park]}")

# 5. Sort by park name in reverse order
print("\nSorted by park name (reverse):")
for park in sorted(squirrels_by_park, reverse=True):
    print(f"{park}: {squirrels_by_park[park]}")
