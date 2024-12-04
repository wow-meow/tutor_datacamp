#!/usr/bin/env python3


def show_workspace_vars():
    """Show all non-callable, non-private variables in the current namespace.

    Note:
    - When run as a script (python show_vars_in_workspace.py), this will only show
      variables defined in this script.
    - When imported in IPython and called as a function, it will show all variables
      in the IPython namespace.
    """
    print("\nWorkspace Variables:")
    print("-------------------")

    # Try to get IPython's namespace if we're in IPython
    try:
        # Get IPython's namespace
        from IPython import get_ipython

        ipython = get_ipython()
        if ipython is not None:
            # We're in IPython, use its namespace
            namespace = ipython.user_ns
        else:
            # We're not in IPython, use globals
            namespace = globals()
    except ImportError:
        # IPython not available, use globals
        namespace = globals()

    # Get all variables that don't start with '_' and aren't callable
    user_variables = {
        name: value
        for name, value in namespace.items()
        # Skip private variables
        if not name.startswith("_")
        # Skip functions and classes
        and not callable(value)
        # Skip IPython's special variables
        and name not in ("In", "Out", "exit", "quit", "get_ipython")
    }

    if not user_variables:
        print("No user variables found. Note:")
        print(
            "1. If you're running this as a script, it can only see variables defined in this script"
        )
        print("2. To see IPython workspace variables, do this instead:")
        print("   - Start IPython")
        print(
            "   - Import this function: from show_vars_in_workspace import show_workspace_vars"
        )
        print("   - Run your other script: %run script1.py")
        print("   - Call this function: show_workspace_vars()")
    else:
        # Print each variable and its type
        for name, value in sorted(
            user_variables.items()
        ):  # Sort by name for consistent output
            print(f"{name}: {type(value).__name__} = {value!r}")

    return user_variables


# If running as a script
if __name__ == "__main__":
    print("Running as standalone script:")
    show_workspace_vars()
    print("\nTo see IPython workspace variables, follow these steps:")
    print("1. Start IPython")
    print(
        "2. Import this function: from show_vars_in_workspace import show_workspace_vars"
    )
    print("3. Run your other script: %run script1.py")
    print("4. Call this function: show_workspace_vars()")
