import numpy as np

# Examples of different string dtypes
print("\nString dtype examples:")
# Object dtype - flexible length strings
str_obj = np.array(["short", "very long string here"], dtype="object")
print("object dtype:", str_obj)

# Fixed-length Unicode strings
str_u4 = np.array(["short", "long"], dtype="U4")  # truncates to 4 chars
print("U4 dtype:", str_u4)

# Longer fixed-length Unicode strings
str_u10 = np.array(["short", "longer text"], dtype="U10")
print("U10 dtype:", str_u10)
