#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().
    If a ValueError message is caught, a corresponding
    message is printed to standard error.
    Args:
        value (int): The integer to print.
    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print('{:d}'.format(value))
        return True

    except ValueError as vler:
        sys.stderr.write("Exception: " + str(vler) + "\n")
        return False

    except TypeError as tper:
        sys.stderr.write("Exception: " + str(tper) + "\n")
        return False
