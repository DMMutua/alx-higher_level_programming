#!/usr/bin/python3
"""
Module 7-base_geometry.
Creates a BaseGeometry class.
"""


class BaseGeometry:
    """Class Containing Public Instance Methods."""

    def area(self):
        """
        Raises: Exception with the message
        'area() is not implemented'.
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates An Integer Value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))

        if value <= 0:
            raise ValueError("{name} must be greater than 0".format(self.name))
