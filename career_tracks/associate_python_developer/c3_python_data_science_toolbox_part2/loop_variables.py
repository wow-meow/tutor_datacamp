#!/usr/bin/env python3

# 1. Loop variables persist after the loop
print("\n1. Loop variable persistence:")
for x in range(3):
    pass
print(f"x still exists: {x}")  # x is still 2

# 2. This can cause issues in subsequent loops
print("\n2. Potential naming conflict:")
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']

for x in numbers:
    print(f"x is {x}")
# x is still 3 here!
x_backup = x
print(f"x is {x_backup}")

for x in letters:  # Using x again, but old value exists
    print(f"x is now {x} (but started from {x_backup})")

# 3. Using del to clean up
print("\n3. Using del to clean up:")
for x in numbers:
    print(f"x is {x}")
del x  # Explicitly remove x

for x in letters:  # x starts fresh
    print(f"x is {x} (started fresh)")

# 4. Alternative: Use different names
print("\n4. Alternative: Different names:")
for num in numbers:
    print(f"num is {num}")

for letter in letters:  # No conflict, different names
    print(f"letter is {letter}")

# 5. Nested loops demonstration
print("\n5. Nested loops:")
# Method 1: Without cleanup (problematic)
print("Method 1 - No cleanup (problematic):")
for i in range(2):
    print(f"Outer i: {i}")
    for i in range(5):  # i from outer loop is overwritten
        print(f"  Inner i: {i}")
    print(f"After inner loop, i is: {i}")  # i is from inner loop!
print(f"Final i: {i}")  # i persists with last value

# Method 2: Using different names (best practice)
print("\nMethod 2 - Different names (recommended):")
for outer_i in range(2):
    print(f"Outer i: {outer_i}")
    for inner_i in range(3):
        print(f"  Inner i: {inner_i}")
    print(f"After inner loop, outer_i is still: {outer_i}")
    del inner_i
del outer_i

# Method 3: Using del (but be careful!)
print("\nMethod 3 - Using del (tricky):")
for i in range(2):
    print(f"Outer i: {i}")
    outer_i = i  # Save outer loop value
    del i  # Delete i
    for i in range(3):
        print(f"  Inner i: {i}")
    print(f"After inner loop, saved outer_i is: {outer_i}")
    del i  # Clean up inner loop i too

# Method 4: Using functions (cleanest scope)
print("\nMethod 4 - Using functions (best scope control):")
def inner_loop(outer_val):
    print(f"Outer value: {outer_val}")
    for i in range(3):
        print(f"  Inner i: {i}")

for i in range(2):
    inner_loop(i)
