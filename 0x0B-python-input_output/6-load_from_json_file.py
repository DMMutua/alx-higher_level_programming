#!/usr/bin/python3
"""Module to Load an Object to a file from a JSON file"""
from json import loads


def load_from_json_file(filename):
    """Load JSON File as Objects to a file"""

    with open(filename, encoding='utf-8') as a_file
        return loads(a_file.read())
