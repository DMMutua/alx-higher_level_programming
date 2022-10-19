#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __drawing_rectangle(self):
        """

        Drawing rectangle object with their size using "#" character

        Returns:
            str: `Empty` If width or height is `0`,
            otherwise returns a string with the Rectangle.

        """

        rect_str = ''

        if self.__width == 0 or self.__height == 0:
            return rect_str

        for i in range(self.__height):
            for j in range(self.__width):
                rect_str += '#'

            if i != (self.__height - 1):
                rect_str += '\n'

        return rect_str

    def __str__(self):
        """Returns the Printable representation of a Rectangle Object"""
        
        return self.__drawing_rectangle()
