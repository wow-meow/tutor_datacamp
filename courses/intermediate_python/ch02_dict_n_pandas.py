#!/usr/bin/env python3

# Import the course packages  
import matplotlib.pyplot as plt

#import numpy as np
import pandas as pd

# Import the two datasets
#gapminder = pd.read_csv("datasets/gapminder.csv")
#brics = pd.read_csv("datasets/brics.csv")

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

europe = dict()
#europe.update((country, capital) for country, capital in zip(countries, capitals))
europe.update(zip(countries, capitals))
print(europe)
europe['italy'] = 'rome'
print(europe)
print(f"italy is in europe: {'italy' in europe}")
del europe['italy']
print(f"italy is in europe: {'italy' in europe}")
europe['italy'] = ''
print(f"italy is in europe: {'italy' in europe}")

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe['france']['capital'])
# Create sub-dictionary data: named data, with the keys 'capital' and 'population'. 
# Set them to 'rome' and 59.83, respectively.
data = {'capital':'rome', 'population': 59.83}
# Add data to europe under key 'italy'
europe['italy'] = data

# extract europe.values() and store it in a variable cap_pop_dict
cap_pop_dict = {v['capital']:v['population'] for v in europe.values()}

df_column_dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'], 
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.512, 17.125, 3.288, 9.596, 1.221],
    'population': [206.1, 145.9, 1339.2, 1404.9, 58.2] }

brics = pd.DataFrame(df_column_dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics)

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

# Panda DataFrame -- Square Bracket
# Print out country column as Pandas Series
print(type(cars['country'])) # type is Series
print(cars['country'])
# Print out country column as Pandas DataFrame
print(type(cars[['country']])) # type is DataFrame
print(cars[['country']])
# Print out DataFrame with country and drives_right columns
print(type(cars[['country', 'drives_right']]))
print(cars[['country', 'drives_right']])
# Print out first 3 observations
print(type(cars[:3])) # type is DataFrame
print(cars[:3])
# Print out fourth, fifth and sixth observation
print(cars[3:6])

# Panda DataFrame -- loc, iloc
# Print out observation for Japan
print(type(cars.loc['JPN'])) # type is Series
print(cars.loc['JPN'])
print(cars.iloc[2])
# Print out observations for Australia and Egypt
print(type(cars.loc[['AUS', 'EG']])) # type is DataFrame
print(cars.loc[['AUS', 'EG']])
print(cars.iloc[[1, 6]])
# Print out the drives_right value of the row corresponding to Morocco (its row label is MOR)
print(type(cars.loc['MOR', 'drives_right'])) # type is numpy bool
print(cars.loc['MOR', 'drives_right'])
print(type(cars.iloc[5, 1])) # type is numpy bool
print(cars.iloc[5, 1])
print(type(cars.loc[['MOR'], ['drives_right']])) # type is pandas DataFrame
print(cars.loc[['MOR'], ['drives_right']])
print(type(cars.iloc[[5], [2]])) # type is pandas DataFrame
print(cars.iloc[[5], [2]])
# Print out a sub-DataFrame, containing the observations for Russia and Morocco
# and the columns country and drives_right
print(cars.loc[['RU', 'MOR'], ['country', 'drives_right']])
print(cars.iloc[[4, 5], [1, 2]])

# It's also possible to select only columns with loc and iloc. In both cases,
# you simply put a slice going from beginning to end in front of the comma:
# Print out the drives_right column as a Series using loc or iloc.
print(type(cars.loc[:, 'drives_right']))
print(cars.loc[:, 'drives_right'])
print(type(cars.iloc[:, 2]))
print(cars.iloc[:, 2])
# Print out the drives_right column as a DataFrame using loc or iloc.
print(type(cars.loc[:, ['drives_right']]))
print(cars.loc[:, ['drives_right']])
print(type(cars.iloc[:, [2]]))
print(cars.iloc[:, [2]])
# Print out both the cars_per_cap and drives_right column as a DataFrame using loc or iloc.
print(type(cars.loc[:, ['cars_per_cap', 'drives_right']]))
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
print(type(cars.iloc[:, [0, 2]]))
print(cars.iloc[:, [0, 2]])