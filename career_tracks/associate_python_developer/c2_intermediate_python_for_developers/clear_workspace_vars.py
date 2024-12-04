#!/usr/bin/env python3


def show_workspace_clearing_methods():
    """Demonstrate different methods to clear IPython workspace variables."""
    print("Methods to clear variables in IPython:")
    print("\n1. Clear all variables:")
    print("%reset")  # Will prompt for confirmation
    print("%reset -f")  # Force reset without confirmation

    print("\n2. Clear specific variables:")
    print("del variable_name")  # Delete a single variable
    print("del var1, var2")  # Delete multiple variables

    print("\n3. Clear only output:")
    print("%clear")  # Clear screen output
    print("cls or clear")  # System clear screen

    print("\n4. Reset and clear output:")
    print("%reset_selective")  # Reset specific variables matching pattern
    print("%reset in")  # Reset input variables only
    print("%reset out")  # Reset output variables only

    print("\n5. Show current variables:")
    print("%who")  # List all variables
    print("%who_ls")  # List all variables as a list
    print("%whos")  # Detailed list of all variables

    print("\n6. Clear variables by type:")
    print("%reset_selective str")  # Reset only string variables
    print("%reset_selective float")  # Reset only float variables

    print("\nNote: In Jupyter notebooks, you can also use:")
    print("from IPython import get_ipython")
    print("get_ipython().magic('reset -f')")


if __name__ == "__main__":
    show_workspace_clearing_methods()
