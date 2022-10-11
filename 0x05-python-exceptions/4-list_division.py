#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    resulting_list = []

    for items in range(list_length):
        try:
            resulting_list.append(my_list_1[item] / my_list_2[item])
        except ZeroDivisionError:
            resulting_list.append(0)
            print('division by 0')
            continue

        except IndexError:
            resulting_list.append(0)
            print('out of range')
            continue

        except TypeError:
            resulting_list.append(0)
            print('wrong type')
            continue

        finally:
            pass

    return new_list
