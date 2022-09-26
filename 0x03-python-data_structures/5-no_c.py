#!/usr/bin/python3

def no_c(my_string):
    """Remove all c's and C's from a string"""
    new_string = ''
    for i in my_string:
        if i != 'C' and i != 'c':
            new_string += i

    return new_string
