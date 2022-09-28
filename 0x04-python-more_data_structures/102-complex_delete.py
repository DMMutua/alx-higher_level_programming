#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys_dict = []

    for k, v in a_dictionary.items():
        if v == value:
            keys.append(k)

    if len(keys_dictionary) is not 0:
        for k in keys_dictionary:
            del a_dictionary[k]

    return a_dictionary
