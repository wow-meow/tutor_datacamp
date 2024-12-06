#!/usr/bin/env python3

# Formatted String Literals ("f" strings)

top_ten_girl_names = [
    (1, "Jada"), (2, "Emily"), (3, "Ava"), (4, "Serenity"), (5, "Claire"),
    (6, "Sophia"), (7, "Sarah"), (8, "Ashley"), (9, "Chaya"), (10, "Abigail"),
]

# Loop over the top_ten_girl_names list and use tuple unpacking to get the top_ten_rank and name.
for top_ten_rank, name in top_ten_girl_names:
    # Print out each rank and name like this Rank #: 1 - Jada where the number 1 is the rank and Jada is the name.
    print(f"Rank #: {top_ten_rank} - {name}")


# Combining multiple strings

boy_names = [
    "Josiah", "Ethan", "David", "Jayden", "Mason",
    "Ryan", "Christian", "Isaiah", "Jayden", "Michael",
]

# The top ten boy names are:  as preamble
preamble = "The top ten boy names are: "
# , and as conjunction
conjunction = ", and"
# Combines the first 9 names in boy_names with a comma and space as first_nine_names
first_nine_names = ", ".join(boy_names[:9])
# Print f-string preamble, first_nine_names, conjunction, the final item in boy_names and a period
print(f"{preamble}{first_nine_names}{conjunction} {boy_names[-1]}.")


# Finding strings in other strings

girl_names = [
    'Jada', 'Emily', 'Ava', 'Serenity', 'Claire',
    'Sophia', 'Sarah', 'Ashley', 'Chaya', 'Abigail',
    'Zoe', 'Leah', 'Hailey', 'Ava', 'Olivia',
    'Emma', 'Chloe', 'Sophia', 'Aaliyah', 'Angela',
    'Camila', 'Savannah', 'Serenity', 'Fatoumata'
    ]

# Store a list of girl_names that start with s: names_with_s
names_with_s = [name for name in girl_names if name.lower().startswith("s")]
print(names_with_s)
# Store a list of girl_names that contain angel: names_with_angel
names_with_angel = [name for name in girl_names if "angel" in name.lower()]
print(names_with_angel)
