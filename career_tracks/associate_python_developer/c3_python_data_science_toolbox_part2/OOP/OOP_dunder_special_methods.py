#!/usr/bin/env python3


class DunderExplanation:
    """Shows why they're called 'dunder' methods"""

    # These are equivalent ways of referring to special methods:

    # 1. Full name: "double underscore init double underscore"
    #    - Too long to say!
    #    - Example: "double underscore init double underscore method"
    def __init__(self):
        pass

    # 2. Shorthand: "dunder init"
    #    - Much easier to say!
    #    - Example: "dunder init method"
    def __str__(self):
        return "I'm a dunder str method!"

    # 3. Other examples of dunder method names:
    #    __add__     -> "dunder add"
    #    __len__     -> "dunder len"
    #    __call__    -> "dunder call"
    #    __enter__   -> "dunder enter"
    #    __exit__    -> "dunder exit"

    # Note: The term became popular because:
    # 1. It's shorter than saying "double underscore" all the time
    # 2. It's clearer than just saying "special methods"
    # 3. It distinguishes these methods from single underscore methods
    #    like _protected_method


class SpecialMethodsDemo:
    """Demonstrates Python's special methods (dunder methods)"""

    def __init__(self, value):
        """Constructor - called when creating new instance
        This is a special method (dunder) that Python calls automatically"""
        self.__value = value  # This is name-mangled to _SpecialMethodsDemo__value
        self.__private = (
            "secret"  # This is name-mangled to _SpecialMethodsDemo__private
        )

    def __private_method(self):
        """Regular private method - will be name-mangled
        This is NOT a special method, just a private one"""
        return "I'm private"

    # Special methods for string representation
    def __str__(self):
        """Called by str() and print()"""
        return f"Value is {self.__value}"

    def __repr__(self):
        """Called in interactive console and containers"""
        return f"SpecialMethodsDemo(value={self.__value})"

    # Special methods for operators
    def __add__(self, other):
        """Called when using + operator"""
        return SpecialMethodsDemo(self.__value + other.__value)

    def __len__(self):
        """Called when using len()"""
        return len(str(self.__value))  # ndigits of the integer


if __name__ == "__main__":
    # Create instances
    obj1 = SpecialMethodsDemo(42)
    obj2 = SpecialMethodsDemo(10)

    print("\nAccessing private attributes:")
    # This works - using mangled name
    print("Mangled private attr:", obj1._SpecialMethodsDemo__private)
    # This works - using mangled method name
    print("Mangled private method:", obj1._SpecialMethodsDemo__private_method())

    print("\nSpecial method calls:")
    # __str__ is called
    print("str(obj1):", str(obj1))
    # __repr__ is called
    print("repr(obj1):", repr(obj1))
    # __add__ is called
    print("obj1 + obj2:", obj1 + obj2)
    # __len__ is called
    print("len(obj1):", len(obj1))

    print("\nName mangling explanation:")
    # Show all attributes of obj1
    print("All attributes:", dir(obj1))
    # Show how private names are mangled
    # type(obj1).__name__ yields "_SpecialMethodsDemo__"
    private_attrs = [attr for attr in dir(obj1) if f"_{type(obj1).__name__}__" in attr]
    print("Private attributes:", private_attrs)

    # Demonstrate that __init__ is special
    print("\nSpecial methods vs private methods:")
    print("Is __init__ mangled?", "_SpecialMethodsDemo__init__" in dir(obj1))  # False
    print(
        "Is __private_method mangled?",
        "_SpecialMethodsDemo__private_method" in dir(obj1),
    )  # True
