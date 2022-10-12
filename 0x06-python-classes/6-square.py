#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Representation of a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of a new Square.
        Attributes:
            size (:obj:`int`, optional): The size of the new square
            as private instance.
            position (:obj: `int`, optional): The position of the new square

        Raise:
            TypeError: If `size` type is not `int`.
            ValueError: if `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getting/& setting current position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        if self.__check_tuple(position) is False \
                or self.__check_indexes(position) is False \
                or self.__check_integers(position) is False \
                or self.__check_values(position) is False:
                    raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def __check_tuple(self, position):
        """check tuple validity"""
        if type(position) is tuple:
            return True

        return False

    def __check_indexes(self, position):
        """check valid index"""
        if len(position) == 2:
            return True

        return False

    def __check_integers(self, position):
        """check tuple content validity"""
        if type(position[0]) is int and type(position[1]) is int:
            return True

    def __check_values(self, position):
        """check values are +ve"""
        if position[0] >= 0 and position[1] >= 0:
            return True

        return False

    def area(self):
        """Returns the Current Area of the Square in question."""
        return self.__size ** 2

    def my_print(self):
        """Prints the Instance of a Square with '#' in STDOUT
        Prints empty line if 'size' is 0
        """
        if self.__size == 0:
            print("")

        if self.__position[1] > 0:
            for i in range(self.__position[1]):
                print('')

        for j in range(1, self.area() + 1):
            if j % self.__size == 1:
                print('{:>{w}}'.format('#', w=self.__position[0] + 1), end='')
            else:
                print('#', end='')

            if j % self.__size == 0 and j > 0:
                print()
