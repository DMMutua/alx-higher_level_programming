#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
# Alternate Code
# try:
#     del _dictionary[key]
#     return (a_dictionary)
# except KeyError:
#     return (a_dictionary)
