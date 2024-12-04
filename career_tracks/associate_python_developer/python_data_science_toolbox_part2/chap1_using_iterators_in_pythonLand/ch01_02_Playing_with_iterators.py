#!/usr/bin/env python3

avengers = ["iron man", "thor", "quicksilver", "hawkeye"]
names = ["stark", "odinson", "maximoff", "barton"]

avengers_enum = enumerate(avengers)
avengers_enum_list = list(avengers_enum)
print(avengers_enum)
print(avengers_enum_list)

avengers_zip = zip(avengers, names)
avengers_zip_list = list(avengers_zip)
print(avengers_zip)
print(avengers_zip_list)

# Use the splat operator '*', nothing printed out
print("\nUse the splat operator '*', nothing printed out")
print(*avengers_enum)
print(*avengers_zip)

"""
Now I can explain why nothing is printed. This is happening because both enumerate() and zip() create iterator objects that can only be consumed once. In your code:

First, you create avengers_enum and immediately convert it to a list with 
`avengers_enum_list = list(avengers_enum)`. This consumes the iterator.

Similarly, you create avengers_zip and immediately convert it to a list with 
`avengers_zip_list = list(avengers_zip)`. This also consumes the iterator.

When you later try to use the splat operator (`*`) on these iterators, 
they are already exhausted (fully consumed), so there's nothing left to print.
To fix this, you need to create fresh iterators if you want to use them again.
"""

# Recreate the iterators
print("""
Once you've gone through all the elements, the iterator is exhausted
and won't yield any more values unless you create a new iterator.""")
avengers_enum = enumerate(avengers)
print(*avengers_enum)
avengers_zip = zip(avengers, names)
print(*avengers_zip)

avengers_enum_iter = iter(avengers_enum)

for index, value in enumerate(avengers, start=100):
    print(f"{index}: {value}")

print()
print(type(dict_iter))
print(type(file_iter))
print(type(int_iter))
print(type(str_iter))
print(type(values_iter))
print(type(avengers_enum_iter))

"""
1. Create a list of tuples from mutants and assign the result to mutant_list. 
Make sure you generate the tuples using enumerate() and turn the result from it 
into a list using list().

2. Complete the first for loop by unpacking the tuples generated 
by calling enumerate() on mutants. 
Use index1 for the index and value1 for the value when unpacking the tuple.

3. Complete the second for loop similarly as with the first, 
but this time change the starting index to start from 1 by passing it 
in as an argument to the start parameter of enumerate(). 
Use index2 for the index and value2 for the value when unpacking the tuple.
"""

# Create a list of strings: mutants
mutants = [
    "charles xavier",
    "bobby drake",
    "kurt wagner",
    "max eisenhardt",
    "kitty pryde",
]

aliases = ["prof x", "iceman", "nightcrawler", "magneto", "shadowcat"]

powers = [
    "telepathy",
    "thermokinesis",
    "teleportation",
    "magnetokinesis",
    "intangibility",
]

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

# Unpack and print the tuple pairs
for index1, value1 in enumerate(mutants):
    print(index1, value1)
del index1, value1

# Change the start index
for index2, value2 in enumerate(mutants, start=1):
    print(index2, value2)
del index2, value2

"""
1. Using zip() with list(), create a list of tuples from the three lists mutants, aliases, 
and powers (in that order) and assign the result to mutant_data.

2. Using zip(), create a zip object called mutant_zip from the three lists mutants, aliases,
and powers.

3. Complete the for loop by unpacking the zip object you created and printing the tuple values.
Use value1, value2, value3 for the values from each of mutants, aliases, and powers, 
in that order.
"""

# Create a list of tuples: mutant_data
mutant_data = list(zip(mutants, aliases, powers))
# Print the list of tuples
print(mutant_data)

# Create a zip object using the three lists: mutant_zip
mutant_zip = zip(mutants, aliases, powers)
# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)


"""
Using * and zip to 'unzip'

There is no unzip function for doing the reverse of what zip() does. 
We can, however, reverse what has been zipped together by using zip() with a little help 
from *! * unpacks an iterable such as a list or a tuple into positional arguments 
in a function call.
"""

# Create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# Print the tuples in z1 by unpacking with *
print(*z1)

# Re-create a zip object from mutants and powers: z1
z1 = zip(mutants, powers)
# 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
result1, result2 = zip(*z1)

# zip(* zip(iterable1, iterable2, iterable3, ...)) --> iterable1, iterable2, iterable3, ...
result1, result2 == zip(*zip(mutants, powers))

# Check if unpacked tuples are equivalent to original tuples
print(result1 == tuple(mutants))
print(result2 == tuple(powers))
