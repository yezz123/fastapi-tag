from typing import get_type_hints as hints


def get_return_type(func):
    """
    Get the return type of a function.
    """
    return hints(func).get("return")
