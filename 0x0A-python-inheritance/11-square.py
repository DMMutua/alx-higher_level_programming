#!/usr/bin/python3
"""Module Defines a Class `Square` That Inherits from `Rectangle`"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class implementing blueprint of a square
    Private Instance attribute `size`
    Public Method area()
    Public
    """

    def __init__(self, size):
        """
        Constructor of Instance of Class square
        Args:
            size (int): The size of the new square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    
    def area(self):
        """Returns the area of object `square`
        Overwrites the area method from `Rectangle`
        """
        return self.__size ** 2

    def __str__(self):
        """
        Public Instance Method
        Overwrites the `super().__str__` method
        Returns: print() and str() representations of a Rectangle Object.
        """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
