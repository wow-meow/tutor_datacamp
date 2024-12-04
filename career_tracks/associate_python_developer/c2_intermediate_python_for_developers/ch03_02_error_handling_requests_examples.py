#!/usr/bin/env python3

import requests
from requests.exceptions import RequestException

# Example 1: Basic GET request (correct way)
print("\nExample 1: Basic GET request")
try:
    # Use proper parameters - no content parameter
    response = requests.get(url="https://app.datacamp.com")
    response.raise_for_status()
    print("Success! Status code:", response.status_code)
except RequestException as e:
    print(f"Error occurred: {e}")

# Example 2: GET request with parameters
print("\nExample 2: GET with parameters")
try:
    response = requests.get(
        url="https://api.github.com/search/repositories",
        params={'q': 'python', 'sort': 'stars'},  # Use params for URL parameters
        headers={'Accept': 'application/json'}     # Use headers when needed
    )
    response.raise_for_status()
    print("Success! Status code:", response.status_code)
except RequestException as e:
    print(f"Error occurred: {e}")

# Example 3: POST request with JSON data
print("\nExample 3: POST with JSON")
try:
    response = requests.post(
        url="https://httpbin.org/post",
        json={'key': 'value'},    # Use json for JSON data
        headers={'Content-Type': 'application/json'}
    )
    response.raise_for_status()
    print("Success! Status code:", response.status_code)
except RequestException as e:
    print(f"Error occurred: {e}")

# Example 4: POST request with form data
print("\nExample 4: POST with form data")
try:
    response = requests.post(
        url="https://httpbin.org/post",
        data={'key': 'value'},    # Use data for form data
    )
    response.raise_for_status()
    print("Success! Status code:", response.status_code)
except RequestException as e:
    print(f"Error occurred: {e}")

# Note: The 'content' parameter is not valid in requests
# This is what NOT to do:
# requests.get(url="https://app.datacamp.com", content=True)  # This will raise TypeError
