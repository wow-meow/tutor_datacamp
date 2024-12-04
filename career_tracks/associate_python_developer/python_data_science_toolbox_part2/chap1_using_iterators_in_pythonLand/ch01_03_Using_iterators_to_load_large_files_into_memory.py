#!/usr/bin/env python3

import pandas as pd
from typing import Iterable as IterableType


# Define count_entries()
def count_entries(csv_file: str = "", c_size: int = 10, colname: str = "") -> dict[str, int]:
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: counts_dict
    counts_dict: dict[str, int] = {}
    # Iterate over the file chunk by chunk
    chunks = pd.read_csv(csv_file, chunksize=c_size, index_col=0)
    for chunk in chunks:
        column = chunk[colname]
        # Iterate over the column in DataFrame
        for entry in column:
            if entry not in counts_dict.keys():
                counts_dict[entry] = 1
            else:
                counts_dict[entry] += 1

    return counts_dict


if __name__ == "__main__":
    # Call count_entries(): result_counts
    result_counts = count_entries("tweets.csv", 10, "lang")
    print(result_counts)

    chunks = pd.read_csv("tweets.csv", chunksize=10, index_col=0)
    print(type(chunks))
    assert isinstance(
        chunks, IterableType
    ), "Assertion failed: chunks should be an iterable"
