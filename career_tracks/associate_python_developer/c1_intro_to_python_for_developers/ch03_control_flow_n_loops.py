#!/usr/bin/env python3

num_beds, sq_foot, rent = (2, 800, 1750)
min_num_beds, min_sq_foot, max_rent = (2, 750, 1900)

# Check the number of beds
if num_beds < min_num_beds:
    print("Insufficient bedrooms")
# Check square feet
elif sq_foot <= min_sq_foot:
    print("Too small")
# Check the rent
elif rent > max_rent:
    print("Too expensive")
# If all conditions met
else:
    print("This looks promising!")

courses = {
    "LLM Concepts": "AI",
    "Introduction to Data Pipelines": "Data Engineering",
    "AI Ethics": "AI",
    "Introduction to dbt": "Data Engineering",
    "Writing Efficient Python Code": "Programming",
    "Introduction to Docker": "Programming",
}

# Loop through the dictionary's keys and values
for key, value in courses.items():
    # Check if the value is "AI"
    if value == "AI":
        print(key, "is an AI course")
    # Check if the value is "Programming"
    elif value == "Programming":
        print(key, "is a Programming course")
    # Otherwise, print that it is a "Data Engineering" course
    else:
        print(key, "is a Data Engineering course")


authors = {
    "Penny Jordan": 200,
    "Nicholas Sparks": 22,
    "Ken Follett": 30,
    "Erskine Caldwell": 25,
    "Wilbur Smith": 32,
    "Judith Krantz": 12,
    "Harold Robbins": 23,
    "J. K. Rowling": 22,
    "Debbie Macomber": 199,
    "Eiichiro Oda": 106,
    "Danielle Steel": 179,
    "Barbara Cartland": 723,
    "Georges Simenon": 570,
    "Corín Tellado": 4000,
    "Clive Cussler": 37,
    "Sidney Sheldon": 21,
    "Dean Koontz": 91,
    "Janet Dailey": 93,
    "Jirō Akagawa": 500,
    "Stephen King": 77,
}

# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, value in authors.items():
    # Check for values less than 25
    if value < 25:
        # Append the author to the list
        authors_below_twenty_five.append(key)

print(authors_below_twenty_five)
