#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Replace An Element of a List at a Specific Position"""

    if idx >=0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
