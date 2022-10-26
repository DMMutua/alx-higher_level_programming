#!/usr/bin/python3
"""Definantions of a text file-reading function"""


def read_filename(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
