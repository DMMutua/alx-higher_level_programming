#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    resulting_list = []

    for item in range(0, list_length):
        try:
            div_result = my_list_1[item] / my_list_2[item]

        except TypeError:
            print('wrong type')
            div_result = 0

        except ZeroDivisionError:
            print('division by 0')
            div_result = 0

        except IndexError:
            print('out of range')
            div_result = 0

        finally:
            resulting_list.append(div_result)

    return resulting_list
