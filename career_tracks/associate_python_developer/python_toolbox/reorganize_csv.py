#!/usr/bin/env python3

"""Reorganize CSV data by appending clock_time column to existing data.

This script:
1. Reads the original CSV with ID and lang columns
2. Extracts clock times from a separate section
3. Combines them into a single DataFrame
4. Saves the reorganized data back to CSV
"""

import pandas as pd
# from typing import List


def reorganize_csv(
    filepath: str,
    output_filepath: str = None,
    colname: str = None,
    nrows: int = 0,
    skiprows: int = 0,
) -> None:
    """Reorganize CSV by appending clock_time column to existing data.

    Args:
        filepath: Path to the CSV file
        output_filepath: Path for the output file. If None, overwrites input file
    """
    # Read the first part (ID and lang)
    df_main = pd.read_csv(filepath, nrows=nrows, index_col=0)

    # Read the clock times (skip header rows and empty lines)
    df_new = pd.read_csv(
        filepath,
        skiprows=skiprows,  # Skip original data + header + empty line
        names=[colname],
        nrows=nrows,
    )  # Read same number of rows as main data

    # Add the new column to main DataFrame
    df_main[colname] = df_new[colname]

    # Determine output path
    output_path = output_filepath if output_filepath else filepath

    # Save combined data
    df_main.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
    print(f"\n{df_main.head(n=10)}")
    print(f"{'\t' * 2}...")
    print(f"\n{df_main.tail(n=10).to_string(header=False)}")


if __name__ == "__main__":
    input_file = "tweets_draft.csv"
    # Create a new file instead of overwriting
    output_file = "tweets_reorganized.csv"
    reorganize_csv(
        input_file, output_file, 
        colname="created_at", nrows=100, skiprows=205
    )
