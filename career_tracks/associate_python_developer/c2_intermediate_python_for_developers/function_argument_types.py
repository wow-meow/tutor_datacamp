#!/usr/bin/env python3


def demo_all_arg_types(
    pos_only_arg1,
    pos_only_arg2,
    /,  # Positional-only parameters
    standard_arg1,
    standard_arg2,  # Standard parameters (both positional and keyword)
    *,
    kw_only_arg1,
    kw_only_arg2,  # Keyword-only parameters
):
    """Demonstrate different argument types in Python functions.

    Args:
        pos_only_arg1: Must be specified by position only
        pos_only_arg2: Must be specified by position only
        standard_arg1: Can be specified by position or keyword
        standard_arg2: Can be specified by position or keyword
        kw_only_arg1: Must be specified by keyword only
        kw_only_arg2: Must be specified by keyword only
    """
    print(f"Positional-only args: {pos_only_arg1}, {pos_only_arg2}")
    print(f"Standard args: {standard_arg1}, {standard_arg2}")
    print(f"Keyword-only args: {kw_only_arg1}, {kw_only_arg2}")


# Valid calls:
print("Valid function calls:")
print("-" * 20)

# 1. All arguments in order (works because positional args are in correct order)
demo_all_arg_types(
    1,
    2,  # pos_only args (by position)
    3,
    4,  # standard args (by position)
    kw_only_arg1=5,  # keyword-only args (by keyword)
    kw_only_arg2=6,
)

print("\n")

# 2. Mix of positional and keyword arguments where allowed
demo_all_arg_types(
    1,
    2,  # pos_only args (must be positional)
    standard_arg1=3,  # standard args (can use keyword)
    standard_arg2=4,  # standard args (can use keyword)
    kw_only_arg1=5,  # keyword-only args (must use keyword)
    kw_only_arg2=6,
)

print("\nInvalid function calls (commented out to prevent errors):")
print("-" * 20)
print("""
# Error: can't use keyword for positional-only parameters
demo_all_arg_types(
    pos_only_arg1=1,        # Error! Can't use keyword
    pos_only_arg2=2,        # Error! Can't use keyword
    standard_arg1=3,
    standard_arg2=4,
    kw_only_arg1=5,
    kw_only_arg2=6
)

# Error: can't use position for keyword-only parameters
demo_all_arg_types(
    1, 2,                   # pos_only args
    3, 4,                   # standard args
    5, 6                    # Error! keyword-only args must use keywords
)
""")
