#!/usr/bin/env python3

import numpy as np
import pandas as pd

df_column_dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.512, 17.125, 3.288, 9.596, 1.221],
    'population': [206.1, 145.9, 1339.2, 1404.9, 58.2]}

brics = pd.DataFrame(df_column_dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics)

# Get the 'area' column of the data frame
# Ideally, we need a pandas series
print('\n')
print(brics['area'])
print(type(brics['area']))
print('\n')
print(brics.loc[:, 'area'])
print(type(brics.loc[:, 'area']))
print('\n')
print(brics.iloc[:, 2])
print(type(brics.iloc[:, 2]))

is_huge = brics['area'] > 8 # pandas series of boolean values
print(is_huge)
print(brics[is_huge])
print(type(brics[is_huge]))
print(brics[brics['area'] > 8])

# Use logical_and(), logical_or(), logical_not() from NumPy
is_area_big = np.logical_and(brics['area'] > 8, brics['area'] < 10) 
print("Countries whose area is a big:")
print(brics[is_area_big])
is_area_big_pop_big = np.logical_and(brics['area'] > 8, brics['population'] > 300) 
print("Countries whose area and population are both big:")
print(brics[is_area_big_pop_big])
is_area_big_pop_small = np.logical_and(brics['area'] > 8, brics['population'] < 300) 
print("Countries whose population density is low:")
print(brics[is_area_big_pop_small])
is_area_small_pop_big = np.logical_and(brics['area'] < 8, brics['population'] > 300)
print("Countries whose population density is high:")
print(brics[is_area_small_pop_big])

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
# Create dictionary my_dict with three key:value pairs: my_dict
df_column_dict = {'countries':names, 'drives_right':dr, 'cars_per_cap':cpc}
# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(df_column_dict)
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

cars.rename(columns={'countries': 'country'}, inplace=True)
cars = cars.reindex(columns=['cars_per_cap', 'country', 'drives_right'])

# Extract the drives_right column as a Pandas Series and store it as dr.
dr = cars['drives_right']
# Use dr, a boolean Series, to subset the cars DataFrame. Store the resulting selection in sel.
sel = cars[dr]
sel = cars[cars['drives_right']]
# Print sel, and assert that drives_right is True for all observations.
print(sel)
assert sel['drives_right'].all() == True

# Select the cars_per_cap column from cars as a Pandas Series and store it as cpc.
print(cars.columns.to_list())
cpc = cars['cars_per_cap']
# Use cpc in combination with a comparison operator and 500. 
# You want to end up with a boolean Series that's True if the corresponding country 
# has a cars_per_cap of more than 500 and False otherwise. 
# Store this boolean Series as many_cars.
many_cars = cpc > 500
# Use many_cars to subset cars, similar to what you did before. 
# Store the result as car_maniac.
car_maniac = cars[many_cars]
# Print out car_maniac to see if you got it right.
print(car_maniac)

# Use the code sample provided to create a DataFrame medium, 
# that includes all the observations of cars 
# that have a cars_per_cap between 100 and 500.
cpc = cars['cars_per_cap']
medium = cars[np.logical_and(cpc > 100, cpc < 500)]
# Print out medium.
print(medium)