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

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
