#!/usr/bin/python3
"""
A module to prints a list in ascending order
"""


class MyList(list):
    """
    A class that customizes the list class
    """

    def print_sorted(self):
        """
        Printing an object 'list' in ascending order.

        Sorting the list and then printing the output.
        """

        if issubclass(MyList, list):
            print(sorted(self))
