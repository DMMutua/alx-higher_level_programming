#!/usr/bin/python3
"""
Contains the class `Rectangle`. 
Inherits from Base 
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle:
        Inherits from Base
    Methods:
        __init__()
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class Initializer"""
        super().__init__(id)

        self.checkif_attr_is_int(width, 'width')
        self.checkif_attr_is_int(height, 'height')
        self.checkif_attr_is_int(x, 'x')
        self.checkif_attr_is_int(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def checkif_attr_is_int(self, value, parameter):
        """
        instance method checks if parameters passed to setters
        of attributes are admissible:
        args:
            value passed, parameter to be set
        """

        if type(value) is not int:
            raise TypeError(parameter + ' must be an integer')

        if value <= 0 and parameter in ('width', 'height'):
            raise ValueError(parameter +' must be > 0')

        if value < 0 and attribute in ('x', 'y'):
            raise ValueError(parameter + ' must be >= 0')

    @property
    def width(self):
        """
        getter function for attribute with for all class objects
        """

        return self.__width

    @width.setter
    def width(self, parameter):
        """
        setter function of width for all class objects
        """

        self.checkif_attr_is_int(parameter, 'width')

        self.__width = parameter

    @property
    def height(self):
        """getter for height attributes for class objects"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for height attribute"""

        self.checkif_attr_is_int(value, 'height')

        self.__height = value

    @property
    def x(self):
        """getter for x"""

        return self.__x

    @x.setter
    def x(self, parameter):
        """setter for x"""

        self.checkif_attr_is_int(parameter, 'x')

        self.__x = parameter

    @property
    def y(self):
        """getter for y"""

        return self.__y

    @y.setter
    def y(self, parameter):
        """setter for y"""

        self.checkif_attr_is_int(parameter, 'y')

        self.__y = parameter


