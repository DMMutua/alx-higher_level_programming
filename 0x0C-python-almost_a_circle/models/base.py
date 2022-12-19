#!/usr/bin/python3
"""
A model that contains a Base Class that manages
the id attribute of all classes that inherit from
Base and avoids duplications.
"""

from os import path
import json


class Base:
    """
    Base class. 
    Attributes:.
        __nb_objects - Private, global.
    Methods:
        constructor, .
    """

    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initializer method of objects of class base:

        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
