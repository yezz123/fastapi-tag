from typing import get_type_hints as hints


def get_return_type(func):
    """
    Get the return type of a function.
    
    Args:
        fn (function): The function to get the return type of.

    Returns:
        type: The return type of the function.
    """
    return hints(func).get("return")
