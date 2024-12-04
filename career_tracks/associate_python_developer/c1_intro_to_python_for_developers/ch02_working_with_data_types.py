#!/usr/bin/env python3

"""
This module demonstrates various list slicing operations in Python.
It shows different ways to slice a list using step values and range specifications,
illustrating how Python's list slicing syntax works.
"""

# import numpy as np

a_list = list(range(7))
print(a_list[::2])
print(a_list[::3])
print(a_list[::1])
print(a_list[:1:])
print(a_list[:2:])

playlist = [
    1,
    "Blinding Lights",
    "The Weeknd",
    2,
    "One Dance",
    "Drake",
    3,
    "Uptown Funk",
    "Mark Ronson",
    4,
    "Closer",
    "The Chainsmokers",
    5,
    "One Kiss",
    "Calvin Harris",
    6,
    "Mr. Brightside",
    "The Killers",
]

# Print all songs in the playlist
print(playlist[1::3])

# Create a dictionary called playlist containing the first two songs,
# in that order, with artist names as keys and their respective songs as values.
playlist_list = playlist  # buffer
playlist = {
    playlist_list[2]: playlist_list[1],
    playlist_list[2 + 3]: playlist_list[1 + 3],
}
print(playlist)

# {key: value for item1, item2 in iterable if condition}
playlist = {
    artist.upper(): song.title()
    for artist, song in zip(playlist_list[2::3], playlist_list[1::3])
    if len(artist) > 3 and artist.startswith("T")
}
print(playlist)

# Ternary operator example with multiple actions
playlist2 = {
    (
        artist.title()
        if len(artist) > 3 and len(artist) < 8
        else (artist.lower() if len(artist) <= 3 else artist.upper())
    ): (song.title() if len(song) < 8 else song.upper())
    for artist, song in zip(playlist_list[2::3], playlist_list[1::3])
}
print(playlist2)

# Add a new song
playlist["Usher"] = "Yeah!"
# Print the songs in the playlist
print(playlist.values())

# Compare: List, Dict, Set, Tuple
hip_hop = ["Drake", "JAY-Z", "50 Cent", "Drake"]
# Create a set
indie_set = {"Kings of Leon", "MGMT", "Stereophonics"}
# Convert hip_hop to a set
hip_hop_set = set(hip_hop)
# Print the indie and hip_hop sets
print(indie_set)
print(hip_hop_set)

# Set:
# - entries are unique, cannot duplicate
# - cannot subset with []
# hip_hop_set[0]  #  <-- TypeError 'set' object is not subscriptable

# Sorting a set
hip_hop_ordered = sorted(hip_hop_set)  # Returns a new ordered list
print(type(hip_hop_ordered))
print(hip_hop_ordered)

# Tuple is immutable, while List, Dict, Set are mutable
hip_hop_tuple = tuple(hip_hop)
print(hip_hop_tuple)
print(hip_hop_tuple[0])
# hip_hop_tuple[0] = "hi"  # <-- TypeError: 'tuple' object does not support item assignment
