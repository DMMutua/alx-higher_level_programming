#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_letters = [
            ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
            ['X', 10], ['V', 5], ['I', 1]
            ]
    number = 0
    last = 0

    for letter in roman_string:
        for element in roman_letters:
            if letter == element[0]:
                if last == 0 or last >= element[1]:
                    num += element[1]

                elif last < element[1]:
                    num += element[1] - (last * 2)


                last = element[1]

    return num
