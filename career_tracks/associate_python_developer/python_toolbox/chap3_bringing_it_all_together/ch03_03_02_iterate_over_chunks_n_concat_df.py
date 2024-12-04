#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv("../csv_files/world_ind_pop_data.csv", chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:
    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop["CountryCode"] == "CEB"]

    # Zip DataFrame columns of interest: pops
    pops = zip(
        df_pop_ceb["Total Population"], df_pop_ceb["Urban population (% of total)"]
    )

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb["Total Urban Population"] = [
        int(tup[0] * tup[1] * 0.01) for tup in pops_list
    ]

    # Convert Year to integer type
    df_pop_ceb["Year"] = df_pop_ceb["Year"].astype(int)

    # Concatenate DataFrame chunk to the end of data: data
    data = pd.concat([data, df_pop_ceb])

# Plot urban population data
ax = data.plot(kind="scatter", x="Year", y="Total Urban Population")
# Force x-axis to use integer ticks
ax.xaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.show()
