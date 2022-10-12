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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """Returns the Current Area of the Square in question."""
        return self.__size ** 2

    def my_print(self):
        """Prints the Instance of a Square with '#' in STDOUT
        Prints empty line if 'size' is 0
        """
        if self.__size == 0:
            print("")

        for length in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print("")
