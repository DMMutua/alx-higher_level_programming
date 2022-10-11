#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    """A function that executes a function safely
    assumption that fct is always a pointer to a function
    Args:
        fct - pointer to a function to execute safely

    Returns:
        result of the function
        Otherwise:
            None if a specified error happens
    """
    try:
        result = fct(*args)

    except ZeroDivisionError:
        result = None
        sys.stderr.write("Exception: division by zero\n")

    except IndexError:
        result = None
        sys.stderr.write("Exception: list index out of range\n")

    return result
