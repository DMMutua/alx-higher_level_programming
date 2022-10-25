#!/usr/bin/python3
"""
Defination of a `Rectangle` class that inherits from `BaseGeometry`.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Subclass to Represent rectangle using BaseGeometry"""

    def __init__(self, width, height):
        """Constructor to initialize new Rectangle Objects
        Args:
             width (`int`, private): The width of the new Rectangle.
            height (`int`, private): The height of the new Rectangle.
        """

        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Public Instance Method
        Returns: Area of a Rectangle Object
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Public Instance Method
        Returns: print() and str() representations of a Rectangle Object.
        """
        rep = "[" + str(self.__class__.__name__) + "]"
        rep += str(self.__width) + "/" + str(self.__height)
        return rep
