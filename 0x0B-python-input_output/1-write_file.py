#!/usr/bin/python3
"""Defination of a file-writing function"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
