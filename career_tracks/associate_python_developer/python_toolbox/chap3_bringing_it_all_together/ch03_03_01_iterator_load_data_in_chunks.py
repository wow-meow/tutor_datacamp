#!/usr/bin/env python3

import pandas as pd
from typing import Iterable as IterableType
import matplotlib.pyplot as plt

# Initialize reader object: df_reader
df_reader = pd.read_csv("../csv_files/world_ind_pop_data.csv", chunksize=10)
assert isinstance(df_reader, IterableType), "`df_reader` must be an iterable"
print(type(df_reader))

# Print two chunks
print(next(df_reader))
print(next(df_reader))

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv("../csv_files/world_ind_pop_data.csv", chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == "CEB"]

# Zip DataFrame columns of interest: pops
df1 = df_pop_ceb[["Total Population", "Urban population (% of total)"]]
pops = zip(
    df_pop_ceb["Total Population"],
    df_pop_ceb["Urban population (% of total)"],
)

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)
print(df1)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb["Total Urban Population"] = [
    int(total_pop * percentage / 100) for total_pop, percentage in pops_list
]

# Convert Year to integer type
df_pop_ceb["Year"] = df_pop_ceb["Year"].astype(int)

# Plot urban population data
ax = df_pop_ceb.plot(kind="scatter", x="Year", y="Total Urban Population")

# Force x-axis to use integer ticks
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.show()
