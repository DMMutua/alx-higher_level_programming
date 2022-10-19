#!/usr/bin/python3

"""

Module to Define a Rectangle Class

"""


class Rectangle:
    """Blueprint representation of a triangle"""

    def __init__(self, width=0, height=0):
        """

        Initialization method of a new Object of Rectangle Class
        Args:
            width (:obj:`int`, optional): The width of the new rectangle.
            height (:obj:`int`, optional): The height of the new rectangle.
        
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get the width of the rectangle"""
        
        return self.__width

    @width.setter
    """

    Checks the parameters and set the size of the Rectangle
        Args:
            value (int): The width of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.
    
    """
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get/Set the height of the rectangle"""
        return self.__height

    @height.setter
    """

    Checks the parameters and set the size of the Rectangle
        Args:
            value (int): The height of the Rectangle.
        Raises:
            TypeError: If `value` type is not `int`.
            ValueError: If `value` is less than `0`.

    """
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
