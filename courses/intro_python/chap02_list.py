#!/usr/bin/env python3

house_areas = ["hallway", 11.25, "kitchen", 18.0,
               "chill zone", 20.0, "bedroom", 10.75,
               "bathroom", 10.50, "poolhouse", 24.5,
               "garage", 15.45]

# Delete the poolhouse items from the list
del house_areas[(6-1)*2 : 6*2]
# Print the updated list
print(house_areas)

# Delete the kitchen items from the list
del house_areas[(2-1)*2]
del house_areas[(2-1)*2]
# Print the updated list
print(house_areas)

# Create list areas
areas_numbersOnly = [11.25, 18.0, 20.0, 10.75, 9.50]

""" Currently, the first element in the areas_copy list is changed and the areas
list is printed out. If you hit the run code button you'll see that, although
you've changed areas_copy, the change also takes effect in the areas list.
That's because areas and areas_copy point to the same list.
"""

# Copy the pointer to the list
areas_numbersOnly_copy = areas_numbersOnly
# Change areas_numbersOnly_copy, original areas_numbersOnly gets changed at the same time
area_backup = areas_numbersOnly[0] # backup, copy the value
areas_numbersOnly_copy[0] = 5.0
# Print areas_numbersOnly
print(areas_numbersOnly)
areas_numbersOnly_copy[0] = area_backup
print(areas_numbersOnly)

""" If you want to prevent changes in areas_copy from also taking effect in
areas, you'll have to do a more explicit copy of the areas list with list() or
by using [:].
"""

# Duplicate the list, deep copy, copy every value explicitly
areas_numbersOnly_deepCopy_1 = list(areas_numbersOnly)
areas_numbersOnly_deepCopy_1[0] = 5.0
print(areas_numbersOnly)

# Duplicate the list, deep copy, copy every value explicitly
areas_numbersOnly_deepCopy_2 = areas_numbersOnly[:]
areas_numbersOnly_deepCopy_2[0] = 5.0
print(areas_numbersOnly)
