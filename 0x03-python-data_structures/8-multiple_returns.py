#!/usr/bin/python3

def multiple_returns(sentence):
    my_tuple = ()
    
    length = len(sentence)
    first_char = sentence[1]

    if length == 0:
        my_tuple = 0, "None"
    else:
        my_tuple = length, first_char

    return my_tuple
