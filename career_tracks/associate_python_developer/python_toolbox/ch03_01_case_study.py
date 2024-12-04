#!/usr/bin/env python3

import pandas as pd

feature_names = [
    "CountryName",
    "CountryCode",
    "IndicatorName",
    "IndicatorCode",
    "Year",
    "Value",
]

row_vals = [
    "Arab World",
    "ARB",
    "Adolescent fertility rate (births per 1,000 women ages 15-19)",
    "SP.ADO.TFRT",
    "1960",
    "133.56090740552298",
]


# z1 = zip(feature_names, row_vals)
# print(next(z1))
# print(next(z1))
# print(*z1)
# print(next(z1))  # StopIteration Signal

# Create a zip object by calling zip() and passing to it feature_names and row_vals.
# Assign the result to zipped_lists.
zipped_lists = list(zip(feature_names, row_vals))
# Create a dictionary from the zipped_lists zip object by calling dict() with zipped_lists.
# Assign the resulting dictionary to rs_dict.
rs_dict = {key: value for key, value in zipped_lists}
zipped_lists = zip(feature_names, row_vals)
rs_dict2 = dict(zipped_lists)

# Print the dictionary
print(rs_dict)
print(rs_dict2)
assert rs_dict == rs_dict2, "Assertion failed: The two dicts should be identical."


# Define lists2dict()
def lists2dict(keys: list, values: list) -> dict:
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""
    # rs_dict = {key: value for key, value in zip(keys, values)}
    zipped_lists = zip(keys, values)
    rs_dict = dict(zipped_lists)
    return rs_dict


# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)
# Print rs_fxn
print(rs_fxn)

row_lists = [
    [
        "Arab World",
        "ARB",
        "Adolescent fertility rate (births per 1,000 women ages 15-19)",
        "SP.ADO.TFRT",
        "1960",
        "133.56090740552298",
    ],
    [
        "Arab World",
        "ARB",
        "Age dependency ratio (% of working-age population)",
        "SP.POP.DPND",
        "1960",
        "87.7976011532547",
    ],
    [
        "Arab World",
        "ARB",
        "Age dependency ratio, old (% of working-age population)",
        "SP.POP.DPND.OL",
        "1960",
        "6.634579191565161",
    ],
    [
        "Arab World",
        "ARB",
        "Age dependency ratio, young (% of working-age population)",
        "SP.POP.DPND.YG",
        "1960",
        "81.02332950839141",
    ],
    [
        "Arab World",
        "ARB",
        "Arms exports (SIPRI trend indicator values)",
        "MS.MIL.XPRT.KD",
        "1960",
        "3000000.0",
    ],
    [
        "Arab World",
        "ARB",
        "Arms imports (SIPRI trend indicator values)",
        "MS.MIL.MPRT.KD",
        "1960",
        "538000000.0",
    ],
    [
        "Arab World",
        "ARB",
        "Birth rate, crude (per 1,000 people)",
        "SP.DYN.CBRT.IN",
        "1960",
        "47.697888095096395",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions (kt)",
        "EN.ATM.CO2E.KT",
        "1960",
        "59563.9892169935",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions (metric tons per capita)",
        "EN.ATM.CO2E.PC",
        "1960",
        "0.6439635478877049",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions from gaseous fuel consumption (% of total)",
        "EN.ATM.CO2E.GF.ZS",
        "1960",
        "5.041291753975099",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions from liquid fuel consumption (% of total)",
        "EN.ATM.CO2E.LF.ZS",
        "1960",
        "84.8514729446567",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions from liquid fuel consumption (kt)",
        "EN.ATM.CO2E.LF.KT",
        "1960",
        "49541.707291032304",
    ],
    [
        "Arab World",
        "ARB",
        "CO2 emissions from solid fuel consumption (% of total)",
        "EN.ATM.CO2E.SF.ZS",
        "1960",
        "4.72698138789597",
    ],
    [
        "Arab World",
        "ARB",
        "Death rate, crude (per 1,000 people)",
        "SP.DYN.CDRT.IN",
        "1960",
        "19.7544519237187",
    ],
    [
        "Arab World",
        "ARB",
        "Fertility rate, total (births per woman)",
        "SP.DYN.TFRT.IN",
        "1960",
        "6.92402738655897",
    ],
    [
        "Arab World",
        "ARB",
        "Fixed telephone subscriptions",
        "IT.MLT.MAIN",
        "1960",
        "406833.0",
    ],
    [
        "Arab World",
        "ARB",
        "Fixed telephone subscriptions (per 100 people)",
        "IT.MLT.MAIN.P2",
        "1960",
        "0.6167005703199",
    ],
    [
        "Arab World",
        "ARB",
        "Hospital beds (per 1,000 people)",
        "SH.MED.BEDS.ZS",
        "1960",
        "1.9296220724398703",
    ],
    [
        "Arab World",
        "ARB",
        "International migrant stock (% of population)",
        "SM.POP.TOTL.ZS",
        "1960",
        "2.9906371279862403",
    ],
    [
        "Arab World",
        "ARB",
        "International migrant stock, total",
        "SM.POP.TOTL",
        "1960",
        "3324685.0",
    ],
]

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts

keys = feature_names
list_of_dicts = [dict(zip(keys, values)) for values in row_lists]
list_of_dicts2 = [lists2dict(keys, values) for values in row_lists]

# Print the first two dictionaries in list_of_dicts
print("\nlist_of_dicts:")
print(list_of_dicts[0])
print(list_of_dicts[1])
print("\nlist_of_dicts2:")
print(list_of_dicts2[0])
print(list_of_dicts2[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts1 = [dict(zip(feature_names, row)) for row in row_lists]
list_of_dicts2 = [lists2dict(feature_names, row) for row in row_lists]
list_of_dicts3 = [
    {key: value for key, value in zip(feature_names, row)} for row in row_lists
]

df1 = pd.DataFrame(list_of_dicts1)
df2 = pd.DataFrame(list_of_dicts2)
df3 = pd.DataFrame(list_of_dicts3)

print()
print(f"df1 == df2: {all(df1 == df2)}")
print(f"df1 == df3: {all(df1 == df3)}")

# Turn list of dicts into a DataFrame: df
# columns_dict[key] = [ value for value in a_dict[key] for a_dict in list_of_dicts for key in feature_names]
col_lists = [[a_dict[key] for a_dict in list_of_dicts] for key in feature_names]
col_lists2 = [[row[i] for row in row_lists] for i, key in enumerate(feature_names)]

data_for_df = {colname: column for colname, column in zip(feature_names, col_lists)}
data_for_df2 = {colname: column for colname, column in zip(feature_names, col_lists2)}

df4 = pd.DataFrame(data_for_df)
df5 = pd.DataFrame(data_for_df2)

print()
print(f"df4 == df5: {all(df4 == df5)}")

# Print the head of the DataFrame
print()
print(df1.head())
