#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    differents = set_1 ^ set_2
    return differents
# Alternative Code
# differents = set_1. symmetric_difference(set_2)
