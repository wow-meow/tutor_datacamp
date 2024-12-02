#!/usr/bin/env python3


class PropertyUnderTheHood:
    """Shows how @property decorator works internally"""

    def __init__(self):
        # The actual value is stored in a private variable
        self.__value = 0

    # Method 1: Traditional way without decorators
    def get_value_old(self):
        return self.__value

    def set_value_old(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self.__value = new_value

    # Method 2: Using property() function directly
    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self.__value = new_value

    # This is what @property does under the hood!
    value = property(get_value, set_value)

    # Method 3: Using @property decorator (syntactic sugar for Method 2)
    @property
    def value_decorated(self):
        """This is equivalent to using property(get_value)"""
        return self.__value

    @value_decorated.setter
    def value_decorated(self, new_value):
        """This is equivalent to property(get_value).setter(set_value)"""
        if new_value < 0:
            raise ValueError("Value cannot be negative")
        self.__value = new_value


if __name__ == "__main__":
    obj = PropertyUnderTheHood()

    # Method 1: Old way (not pythonic)
    print("\nOld way (not pythonic):")
    obj.set_value_old(42)
    print("get_value_old():", obj.get_value_old())

    # Method 2: Using property() function
    print("\nUsing property() function:")
    obj.value = 43  # Calls set_value internally
    print("value:", obj.value)  # Calls get_value internally

    # Method 3: Using @property decorator
    print("\nUsing @property decorator:")
    obj.value_decorated = 44  # Calls the setter method
    print("value_decorated:", obj.value_decorated)  # Calls the getter method

    # Demonstrating validation
    print("\nTrying to set negative values:")
    try:
        obj.value = -1  # Should raise ValueError
    except ValueError as e:
        print("property() error:", str(e))

    try:
        obj.value_decorated = -1  # Should raise ValueError
    except ValueError as e:
        print("@property error:", str(e))

    # Showing that they're the same under the hood
    print("\nUnder the hood:")
    print("property() type:", type(PropertyUnderTheHood.value))
    print("@property type:", type(PropertyUnderTheHood.value_decorated))
    print(
        "Are they the same type?",
        type(PropertyUnderTheHood.value) == type(PropertyUnderTheHood.value_decorated),
    )
