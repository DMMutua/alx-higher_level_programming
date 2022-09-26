#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return "None"

    else:
        max_interim = my_List[0]

        for i in my_list:
            if i > max_interim:
                max_interim = i

        return max_interim 

