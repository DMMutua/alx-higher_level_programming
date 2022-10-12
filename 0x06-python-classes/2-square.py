#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0):
        """Initialization of a new Square.

        Attributes:
            size (:obj:`int`, optional): The size of the new square
            as private instance.

        Raise:
            TypeError: If `size` type is not `int`.
            ValueError: if `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
