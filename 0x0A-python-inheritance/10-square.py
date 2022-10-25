#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class implementing blueprint of a square"""

    def __init_(self, size):
        """
        Constructor of Instance of Class square
        Args:
            size (int): The size of the new square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
