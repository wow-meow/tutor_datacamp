### Special methods and Dunder functions

#### Dunder: Double UNDERscore

The term "dunder" is a community-created shorthand that emerged because:

1. Original name was too verbose:
    - `__init__` → "double underscore init double underscore"
    - That's a mouthful!

2. Shorthand is more practical:
    - `__init__` → "dunder init"
    - `__str__` → "dunder str"
    - `__len__` → "dunder len"

3. It helps distinguish between:
    - Dunder methods (`__init__`): Special Python methods
    - Single underscore (`_protected`): Convention for protected
    - No underscore (`public`): Regular public methods

The term became popular in the Python community around 2006-2007 and is now widely used in Python documentation, talks, and discussions. It's much easier to say "dunder method" than "double underscore method" or even "special method"!

#### Explanation

The key difference is:

1. Regular Private Methods (single leading and trailing underscore):

```python
def __private_method(self):
```
- Gets name-mangled to `_ClassName__private_method`
- Used to indicate "private" members
- Python changes the name to prevent accidental access

2. Special Methods (double leading AND trailing underscores):

```python
def __init__(self):
```

- Also called "dunder" methods (double underscore)
- NOT name-mangled because they're meant to be found by Python
- Provide special behavior (like initialization, string representation, operators)
- Python looks for these specific names to implement language features

Common special methods:

- init: Constructor
- str: String representation (for users)
- repr: String representation (for developers)
- add: Addition operator (+)
- len: Length function

As you can see in the output:

- `__private_method` is mangled to `_SpecialMethodsDemo__private_method`
- `init` stays as `init` (no mangling)
- Special methods like `str`, `add` also stay unmangled

This is why you can always call `obj.__init__()` but not `obj.__private_method()` directly!


### main check

Here's what's happening:

1. In Python, `__name__` is a special variable that:
    - Equals "__main__" when the file is run directly
    - Equals the module's name when the file is imported

2. if `__name__` == "`__main__`": is used to:
    - Run code only when the file is executed directly
    - Skip code when the file is imported as a module

Common uses:

```python
if `__name__` == "`__main__`":
    # Put test code here
    # Put example usage
    # Put command-line interface code
```

This pattern allows you to:

- Write reusable modules with functions/classes
- Include test code in the same file
- Make files that can work both as modules and standalone scripts

In the example:

- When running `main_check.py` directly: `__name__` == "`__main__`", so test code runs
- When importing `main_check.py`: `__name__` == "`main_check`", so test code is skipped

This is a Python best practice that helps you:

- Keep test code with your module
- Prevent test code from running when importing
- Make modules more reusable

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
