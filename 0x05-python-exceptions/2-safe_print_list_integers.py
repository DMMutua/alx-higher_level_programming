#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_items = 0

    for item in range(x):
        try:
            if type(my_list[item]) is int and printed_items != x:
                    print('{:d}'.format(my_list[item]), end='')
                    printed_items += 1
        except TypeError:
            continue

    print()

    return printed_items
