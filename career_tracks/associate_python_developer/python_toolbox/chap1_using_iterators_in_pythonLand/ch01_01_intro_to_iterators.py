#!/usr/bin/env python3

word = "Data"
str_iter = iter(word)

numbers = [1, 2, 3, 4]
int_iter = iter(numbers)
sum(numbers)
print(tuple(numbers))
print(*int_iter)

pythonistas = {"hugo": "Hello, World!", "francis": "Hey, bro!"}
dict_iter = iter(pythonistas)
for key, value in pythonistas.items():
    print(key, value)

a_textIOWrapper = open("README.md", mode="r", encoding="utf-8")
file_iter = iter(a_textIOWrapper)
# print(next(it_file))

# Create a list of strings: flash
flash = ["jay garrick", "barry allen", "wally west", "bart allen"]

# Create a for loop to loop over flash and print the values in the list.
# Use person as the loop variable.
for x in flash:
    print(x)
del x

# Create an iterator for the list flash and assign the result to superhero.
superhero = iter(flash)
# Print each of the items from superhero using next() 4 times.
print(next(superhero))
print(next(superhero))
print(next(superhero))
print(next(superhero))

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for x in range(3):
    print(x)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10**100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))

# Create a range object that would produce the values from 10 to 20 using range().
# Assign the result to values.
values = range(10, 21, 1)

# Use the list() function to create a list of values from the range object values.
# Assign the result to values_list.
values_list = list(values)

# Use the sum() function to get the sum of the values from 10 to 20 from the range object values.
# Assign the result to values_sum.
values_sum = sum(values)

values_iter = iter(values)
print(*values_iter)
print(values_list)
print(values_sum)
