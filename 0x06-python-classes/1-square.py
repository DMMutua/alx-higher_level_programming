#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size):
        """Initialization of a new Square.
        Args:
            size (int): The size of the new square kept private.
        """
        self.__size = size
