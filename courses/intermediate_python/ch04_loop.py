#!/usr/bin/env python3

import numpy as np
import pandas as pd

# Create the variable offset with an initial value of -6.
offset = -6 
# Code a while loop that keeps running as long as offset is not equal to 0. 
# Inside the while loop: Print out the sentence "correcting...".
# Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
# Finally, still within your loop, print out offset so you can see how it changes.
while offset != 0 :
    print("correcting...")
    if offset > 0 :
        offset = offset - 1
    else :
        offset = offset + 1
    print(f"offset updated: {offset}")

heights = [1.73, 1.68, 1.71, 1.89]
fam     = [1.73, 1.68, 1.71, 1.89]
for label, val in enumerate(heights) :
    print(f"index {label}: {val}")
    
for label, val in enumerate("family") :
    print(f"index {label}: {val.capitalize()}")

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
# Code the for loop
for label, val in enumerate(areas, start=1) :
    print(f"room {label}: {val}")

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
# Write a for loop that goes through each sublist of house and prints out 
# the x is y sqm, where x is the name of the room and y is the area of the room.
for val in house :
    print(f"the {val[0]} is {val[1]} sqm")
    
# iterate through a dict
world = { 'afganistan':30.55,
          'albania':2.77,
          'algeria':39.21 }
for k, v in world.items() :
    print(f"{k} -- {v}")
    
# 2D numpy array
heights = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
weights = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = weights / heights ** 2
print(bmi)
meas = np.array([heights, weights])
print(meas.shape)
for val in meas :
    print(val)
# Need a numpy function to iterate 
for val in np.nditer(meas) :
    print(val)
    
# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
# Iterate over europe
for k, v in europe.items() :
    print(f"the capital of {k} is {v}")

# Import numpy as np
import numpy as np
# For loop over np_height
for val in heights :
    print(f"{val} inches")
    
# height in inch, weight in pounds (lb), age in year
baseball = [[74.0, 180.0, 22.99],
            [74.0, 215.0, 34.69],
            [72.0, 210.0, 30.78],
            [69.0, 209.0, 30.77],
            [71.0, 200.0, 35.07],
            [76.0, 231.0, 30.19]]
# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)
# Print out the type of np_baseball
print(type(np_baseball))
# Print out the shape of np_baseball
print(np_baseball.shape)
# For loop over np_baseball
for val in np.nditer(np_baseball) :
    print(val)

'''    '''

df_column_dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.512, 17.125, 3.288, 9.596, 1.221],
    'population': [206.1, 145.9, 1339.2, 1404.9, 58.2]}

brics = pd.DataFrame(df_column_dict)
brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics)

print()
for val in brics :
    print(val)

print()
for label, row in brics.iterrows() :
    print(label)
    print(row)
    print()

print()
for label, row in brics.iterrows() :
    print(f"{label}: {row['capital']}")

print()
for label, row in brics.iterrows() :
    # Creating a series on every iteration
    brics.loc[label, 'name_length'] = len(row['country'])

# astype() the most reliable way to convert column types in DataFrames
brics['name_length'] = brics['name_length'].astype('int64')
# Remove a column from a dataframe 
brics.drop('name_length', axis=1, inplace=True)
# Use apply() method because the loop iteration is inefficient
brics['name_length'] = brics['country'].apply(len)

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

# Write a for loop that iterates over the rows of cars and on each iteration 
# perform two print() calls: one to print out the row label and one to print 
# out all of the rows contents.
for label, row in cars.iterrows() :
    print(label)
    print(row)

# Using the iterators lab and row, adapt the code in the for loop such that 
# the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
# The output should be in the form "country: cars_per_cap". 
# Make sure to print out this exact string (with the correct spacing).
# You can use str() to convert your integer data to a string so that you can print it 
# in conjunction with the country label.
for label, row in cars.iterrows() :
    print(f"{label}: {row['cars_per_cap']}")

# Use a for loop to add a new column, named COUNTRY, that contains a uppercase version 
# of the country names in the "country" column. You can use the string method upper() for this.
for label, row in cars.iterrows() :
    cars.loc[label, 'COUNTRY'] = str.upper(row['country'])
# To see if your code worked, print out cars. Don't indent this code, so that it's not part 
# of the for loop.
print(cars)

""" Using iterrows() to iterate over every observation of a Pandas DataFrame is easy to understand, 
but not very efficient. On every iteration, you're creating a new Pandas Series.

If you want to add a column to a DataFrame by calling a function on another column, 
the iterrows() method in combination with a for loop is not the preferred way to go. 
Instead, you'll want to use apply().
"""

cars.drop('COUNTRY', axis=1, inplace=True)
cars['COUNTRY'] = cars['country'].apply(str.upper)