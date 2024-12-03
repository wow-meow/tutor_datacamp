#!/usr/bin/env python3

"""Practice with pandas Series and CSV reading.

This module demonstrates:
- Creating and manipulating pandas Series
- Reading CSV files in chunks
- Handling different file encodings
"""

import pandas as pd
from pprint import pprint

# Initialize an empty Series
tweet_time = pd.Series(dtype=object)

# Read CSV in chunks
chunks = pd.read_csv("tweets.csv", chunksize=10, encoding="utf-8")

# Process each chunk
colname = "created_at"
# colname = 'lang'
for chunk in chunks:
    # Extract the created_at column
    column = chunk[colname]
    # Concatenate with existing Series
    tweet_time = pd.concat([tweet_time, column], ignore_index=True)

# Display first few entries
print("\ntweet_time:")
print(tweet_time.head(n=10).to_string())
print(f"{'\t' * 2}...\n")
print(tweet_time.tail(n=10).to_string())

# Display Series info
print("\nSeries info:")
tweet_time.info()

# Extract the created_at column from df: tweet_time
df = pd.read_csv("tweets.csv", nrows=100, encoding="utf-8")
tweet_time_series = df["created_at"]
print()
print(type(tweet_time_series))

# Extract the clock time: tweet_clock_time
tweet_clock_time = [entry[11:19] for entry in tweet_time]
print(type(tweet_clock_time))
# Print first few and last few times
print("\nClock times:")
print("\n".join(tweet_clock_time[:5]))
print(f"{'\t' * 2}...")
print("\n".join(tweet_clock_time[-5:]))
print()

# Using string formatting with list comprehension
print("\nUsing string formatting sep_str.join() + generator expr:")
print(
    "\n".join(
        f"Time {i:3d}: {time}"
        for i, time in enumerate(tweet_clock_time, start=1)
        if i < 11 or i > 90
    ),
)

# These are equivalent:
print("\n".join(["a", "b", "c"]))  # Result: 'a\nb\nc'
print("---".join(["a", "b", "c"]))  # Result: 'a---b---c'
# With a generator:
print("\n".join(str(x) for x in range(3)))  # Result: '0\n1\n2'

# {i:<3d} for left alignment
# {i:>3d} for explicit right alignment (default)
# {i:^3d} for center alignment
# {i:03d} to pad with zeros instead of spaces

print("\nUsing splat operator + generator expr:")
print(
    *(
        f"Time {i:3d}: {time}"
        for i, time in enumerate(tweet_clock_time, start=1)
        if i < 11
    ),
    sep="\n",
)
print("\t" * 2, "...")
print(
    *(
        f"Time {i:3d}: {time}"
        for i, time in enumerate(tweet_clock_time, start=1)
        if i > 90
    ),
    sep="\n",
)


# # Using pandas Series for tabular display:
# print("\nUsing pandas Series for tabular display:")
# print(pd.Series(tweet_clock_time).to_string())

# # Using pprint for more complex structures:
# print("\nUsing pprint for more complex structures: ")
# pprint(tweet_clock_time)
