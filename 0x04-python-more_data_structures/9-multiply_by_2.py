#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    value_doubled_dictionary = {}

    for key in a_dictionary:
        value_doubled = (a_dictionary.get(key)) * 2
        value_doubled_dictionary.update({key: value_doubled})

    return (value_doubled_dictionary)

# Alternatively; you can create a copy of a_dictionary, access and double
# the values in the copy, and return the new value-doubled copy
