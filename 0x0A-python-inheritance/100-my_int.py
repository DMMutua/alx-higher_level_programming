#!/usr/bin/python3
"""
Module: 11-my_int
Defination of a class MyInt that inherits from class `int`.
"""


class MyInt(int):
    """
    Blueprint of `MyInt` objects.
    Public Instance Methods to:
        Invert int operator `==`.
        Invert int operator `!=`.
    """

    def __eq__(self, value):
        """Overrides `==` operator with `!=` behavior."""

        return self.real != value

    def __ne__(self, value):
        """Overriding `!=` operator with `==` behavior."""

        return self.real == value
