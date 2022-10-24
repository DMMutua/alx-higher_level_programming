#!/usr/bin/python3
"""Defining an object attribute lookup function"""


def lookup(obj):
    """
    Returning the list of available attributes and methods of an object
    """

    return (dir(obj))
