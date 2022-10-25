#!/usr/bin/python3
"""
An Integer validator module

Class : `BaseGeometry`
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
        """
        Validates An Integer Value

        Args:
            name (str): The name of the value.
            value (int): The value

        Raises:
                TypeError: if `value` is not integer
                ValueError: if `value` is less than or equal to zero.
        """

        if type(value) is not int:
            raise TypeError(name + ' must be an integer')

        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
