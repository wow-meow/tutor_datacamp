#!/usr/bin/env python3


class Example:
    """Example class demonstrating Python's access conventions"""

    def __init__(self):
        self.public_attr = "Anyone can see this"
        self._protected_attr = "Please don't access directly"
        self.__private_attr = "Name will be mangled"

    def public_method(self):
        """Anyone can call this"""
        return f"Public method: {self.public_attr}"

    def _protected_method(self):
        """Please don't call this from outside"""
        return f"Protected method: {self._protected_attr}"

    def __private_method(self):
        """Name will be mangled to _Example__private_method"""
        return f"Private method: {self.__private_attr}"


# Usage example:
e = Example()
print("Public:", e.public_attr)  # Works fine
print("Public:", e.public_method())  # Works fine

print("Protected:", e._protected_attr)  # Works, but shouldn't do this
print("Protected:", e._protected_method())  # Works, but shouldn't do this

# print("Private:", e.__private_attr)  # AttributeError!
# print("Private method:", e.__private_method())  # AttributeError!
print(
    "Private (mangled):", e._Example__private_attr
)  # Works, but really shouldn't do this
print(
    "Private (mangled):", e._Example__private_method()
)  # Works, but really shouldn't do this
