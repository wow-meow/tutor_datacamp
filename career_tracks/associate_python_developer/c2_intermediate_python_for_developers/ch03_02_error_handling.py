#!/usr/bin/env python3

import pandas as pd

# Create DataFrame with list values for each column
products = pd.DataFrame({"ID": ["ABC1"], "price": [2.99]})
print("\nDataFrame contents:")
print(products)
tag_column = products["tag"]

# # Try to access non-existent "tag" column with error handling
# try:
#     tag_column = products["tag"]
# except KeyError as e:
#     print(
#         f"\nError: KeyError {e} : Column \'tag\' not found in DataFrame. "
#         f"Available columns are: {list(products.columns)}"
#     )
#     # Optionally, you could create the column if needed:
#     # products_2["tag"] = ["sale"]  # Add a new "tag" column
