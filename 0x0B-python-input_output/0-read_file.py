#!/usr/bin/python3
"""Definantions of a text file-reading function."""


def read_filename(filename=""):
    """Print the contents of a UTF8 text file to stdout"""
    
    with open(filename, "r", encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end = '')
