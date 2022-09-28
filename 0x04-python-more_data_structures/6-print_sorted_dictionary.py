#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for sorted_key in sorted(a_dictionary):
        print("{}: {}".format(sorted_key, a_dictionary[sorted_key]))
