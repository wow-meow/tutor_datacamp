#!/usr/bin/env python3


class ExampleClass:
    """Example class demonstrating different ways to define attributes"""

    # 1. Class attributes (shared by all instances)
    class_public_attr = "Class-level public attribute"
    _class_protected_attr = "Class-level protected attribute"
    __class_private_attr = "Class-level private attribute"

    def __init__(self, name: str):
        # 2. Instance attributes (unique to each instance)
        self.public_attr = "Instance-level public attribute"
        self._protected_attr = "Instance-level protected attribute"
        self.__private_attr = "Instance-level private attribute"

        # 3. Dynamic attribute assignment
        setattr(self, "dynamic_attr", "Dynamically added attribute")

        # 4. Instance-specific value
        self.name = name


class ExampleClassWithProperties:
    """Example class demonstrating properties"""

    def __init__(self):
        # Private backing field
        self.__value = 0

    # 5. Property decorator (getter)
    @property
    def value(self):
        """Get the value"""
        return self.__value

    # Property setter
    @value.setter
    def value(self, new_value):
        """Set the value with validation"""
        if new_value < 0:
            raise ValueError("Error: Value cannot be negative")
        self.__value = new_value


# Usage examples
if __name__ == "__main__":
    # Class attributes can be accessed directly on the class
    print("Class attribute:", ExampleClass.class_public_attr)

    # Instance attributes need an instance
    e1 = ExampleClass("instance1")
    e2 = ExampleClass("instance2")

    # Class attributes are shared
    ExampleClass.class_public_attr = "Modified class attribute"
    print("e1 class attr:", e1.class_public_attr)  # Shows modified value
    print("e2 class attr:", e2.class_public_attr)  # Shows same modified value

    # Instance attributes are unique
    e1.public_attr = "Modified instance 1"
    print("e1 instance attr:", e1.public_attr)  # Shows modified value
    print("e2 instance attr:", e2.public_attr)  # Shows original value

    # Use setattr to create a new attribute for an instance 'dynamically'
    print("\nDynamic attribute examples:")
    # Method 1: Using setattr function
    attr_name1 =  "dynamic_attr1"
    setattr(e1, attr_name1, "Added using setattr")
    print("Dynamic attr1:", e1.dynamic_attr1)

    # Method 2: Direct assignment
    e1.dynamic_attr2 = "Added directly"
    print("Dynamic attr2:", e1.dynamic_attr2)

    # Method 3: Using setattr with existing attribute
    setattr(e1, "name", "New name")  # Modifying existing attribute
    print("Modified name:", e1.name)

    # Check if e2 has these attributes
    print("\nChecking e2 for dynamic attributes:")
    print("e2 has dynamic_attr1?", hasattr(e2, "dynamic_attr1"))  # False
    print("e2 has dynamic_attr2?", hasattr(e2, "dynamic_attr2"))  # False

    # Using properties
    p = ExampleClassWithProperties()
    p.value = 42  # Uses setter
    print("Property value:", p.value)  # Uses getter

    try:
        p.value = -1  # Will raise ValueError
    except ValueError as e:
        print("Validation error:", str(e))
