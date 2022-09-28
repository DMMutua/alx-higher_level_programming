#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_sum = 0
    uniq_list = []
    for number in my_list:
        if number not in uniq_list:
            uniq_list.append(number)
    for number in uniq_list:
        uniq_sum += number
    return uniq_sum

# Alternative Code: return sum(set(my_list))
