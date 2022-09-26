#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copyof_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return copyof_list

    copyof_list[idx] = element
    return copyof_list
