### Property Decorators

Ran terminal command

```shell
cd d:/Users/lh/Workspaces/tutor_datacamp/career_tracks/associate_python_developer/python_toolbox

python property_decorators.py
```

```console stdout

Old way (not pythonic):
get_value_old(): 42

Using property() function:
value: 43

Using @property decorator:
value_decorated: 44

Trying to set negative values:
property() error: Value cannot be negative
@property error: Value cannot be negative

Under the hood:
property() type: <class 'property'>
@property type: <class 'property'>

Are they the same type? True
```

The magic of @property works through Python's descriptor protocol. Here's what happens:

The @property decorator is actually syntactic sugar for the property() built-in function:

```python
# These two are equivalent:
@property
def value(self): ...

value = property(value)
```

When you use the property decorator:

```python
@property
def value(self):
    return self.__value

@value.setter
def value(self, new_value):
    self.__value = new_value
```

Python internally converts this to:

```python
value = property(get_value)  # Creates a property object
value = value.setter(set_value)  # Adds setter to the property
```

When you access the attribute:

`obj.value` → Python sees it's a property and calls the getter method
`obj.value = x` → Python sees it's a property and calls the setter method

This is why you can:

- Access it like a regular attribute: `obj.value`
- Add validation in the setter: `if new_value < 0: raise ValueError`
- Compute values on the fly in the getter
- Keep the actual data private: `self.__value`

The output shows that both methods (using property() directly or @property decorator) create the same type of object under the hood: `<class 'property'>`.
